<template>
  <div>
    <a-breadcrumb separator="">
      <a-breadcrumb-item>
        <router-link to="/store/index">当前位置：首页</router-link>
      </a-breadcrumb-item>
      <a-breadcrumb-separator>></a-breadcrumb-separator>
      <a-breadcrumb-item> 图片库 </a-breadcrumb-item>
    </a-breadcrumb>
    <a-divider></a-divider>
    <div>
          <swiper :options="swiperOption">
            <swiper-slide></swiper-slide>
            <swiper-slide></swiper-slide>
            <!--以下看需要添加-->
            <div class="swiper-scrollbar"></div> //滚动条
            <div class="swiper-button-next"></div> //下一项
            <div class="swiper-button-prev"></div> //上一项
            <div class="swiper-pagination"></div> //标页码
          </swiper>
   </div>
  </div>
</template>
<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'
export default {
  name: "index",
  components: {
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  },
  data () {
    return {
      swiperOption: {
        // 分页器配置
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        // 设定初始化时slide的索引
        initialSlide: 0,
        //Slides的滑动方向，可设置水平(horizontal)或垂直(vertical)
        direction: 'horizontal',
        // 自动切换图配置
        autoplay: {
          delay: 5000,
          stopOnLastSlide: false,
          disableOnInteraction: true
        },
        // 箭头配置
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
        // 环状轮播
        loop: true,
        slidesPerView: 'auto',
        loopedSlides: 3,
        loopAdditionalSlides: 0,
        // 一个屏幕展示的数量
        slidesPerView: 1,
        // 间距
        // spaceBetween: 26,
        // 修改swiper自己或子元素时，自动初始化swiper
        observer: true,
        // 修改swiper的父元素时，自动初始化swiper
        observeParents: true
      }
    }
  }
}
</script>
<style scope>
.ant-breadcrumb {
  font-size: 16px;
}

.ant-divider-horizontal {
  margin-top: 16px !important;
  margin-bottom: 16px !important;
}
</style>