import { BadRequestException } from "@nestjs/common";
import { MulterOptions } from "@nestjs/platform-express/multer/interfaces/multer-options.interface";
import { diskStorage } from 'multer';
import { extname } from 'path';

export const multerConfig: MulterOptions = {
    storage: diskStorage({
        destination: './upload',
        filename: (req, file, cb) => {
            const randomName = Array(32)
            .fill(null)
            .map(() => Math.round(Math.random() * 16).toString(16))
            .join('');
            return cb(null, `${randomName}${extname(file.originalname)}`);
        },
    }),
    fileFilter: (req, file, cb) => {
        if (!file.mimetype.match(/\/(jpg|jpeg|png|gif)$/)) {
            cb(new BadRequestException('Solo se permiten archivos de imagen.'), false);
        } else {
            cb(null, true);
        }
    },
    limits: {
        fileSize: 1024 * 1024 * 5, // 5mb
    },
};