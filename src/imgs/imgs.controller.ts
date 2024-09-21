import { Controller, Post, UploadedFile, UseInterceptors } from '@nestjs/common';
import { ImgsService } from './imgs.service';
import { FileInterceptor } from '@nestjs/platform-express';
import { multerConfig } from 'src/multer.config';

@Controller('imgs')
export class ImgsController {

    @Post('/upload')
    @UseInterceptors(FileInterceptor('file', multerConfig))
    upload(@UploadedFile() file){
        return {
            originalname: file.originalname,
            filename: file.filename,
            path: file.path,   
        }
    }
}
