import { Controller, Post, UploadedFile, UseInterceptors } from '@nestjs/common';
import { ImgsService } from './imgs.service';
import { FileInterceptor } from '@nestjs/platform-express';
import { multerConfig } from 'src/multer.config';
import { File } from 'src/types/global';

@Controller('imgs')
export class ImgsController {
    constructor(private readonly imgsService: ImgsService) {}

    @Post('/upload')
    @UseInterceptors(FileInterceptor('file', multerConfig))
    upload(@UploadedFile() file: File){
        return this.imgsService.upload(file);
    }
}
