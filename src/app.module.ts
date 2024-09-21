import { Module } from '@nestjs/common';
import { ImgsModule } from './imgs/imgs.module';

@Module({
  imports: [ImgsModule],

})
export class AppModule {}
