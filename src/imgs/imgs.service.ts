import { Injectable } from '@nestjs/common';

@Injectable()
export class ImgsService {
    upload(){
        return 'file uploaded';
    }
}
