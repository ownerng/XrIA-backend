import { Module } from '@nestjs/common';
import { ImgsController } from './imgs.controller';
import { ImgsService } from './imgs.service';

@Module({
  controllers: [ImgsController],
  providers: [ImgsService]
})
export class ImgsModule {}
