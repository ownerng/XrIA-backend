import { Injectable } from '@nestjs/common';
import { File } from 'src/types/global';

// Este tipo viene de la instalación de @types/express
@Injectable()
export class ImgsService {
    upload(file: File) {
        return {
            message: 'File uploaded',
            filename: file.filename,
        };
    }
}