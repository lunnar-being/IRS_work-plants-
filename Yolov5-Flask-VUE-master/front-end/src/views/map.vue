<template>
  <div>
    <a-breadcrumb separator="">
      <a-breadcrumb-item>
        <router-link to="/store/index">当前位置：首页</router-link>
      </a-breadcrumb-item>
      <a-breadcrumb-separator>></a-breadcrumb-separator>
      <a-breadcrumb-item> 燕园地图浏览 </a-breadcrumb-item>
    </a-breadcrumb>
    <a-divider></a-divider>
    <div class="content">
      <div class="amap-wrapper">
        <el-amap
          class="amap-box"
          :zoom="zoom"
          :center="center"
          :mapStyle="mapStyle"
          :amap-manager="amapManager"

          :events='events'
        >
        <el-amap-ground-image  v-for="groundimage in groundimages" :key="groundimage.id" :url="groundimage.url" :bounds="groundimage.bounds" clickAble="true"></el-amap-ground-image>
        </el-amap>
      </div>
    </div>
  </div>
</template>
<script>
import location from "../../public/image/flower1.jpg";
import {AMapManager, lazyAMapApiLoaderInstance} from 'vue-amap'
// import VueAMap from "vue-amap";
// import AMap from 'vue-amap'
// const AMap=require('vue-amap')

let amapManager = new AMapManager();
export default {
  name:'Amap',
  data() {
    const _this=this;
    return {
      map:null,
      amapManager,
      center: [116.3059, 39.9869], //地图中心点坐标
      zoom: 16, //初始化地图显示层级
      mapStyle: "amap://styles/8b6be8ec497009e17a708205348b899a", //设置地图样式
      markers: [],
      windows: [],
      window: "",
      groundimages: [//
                    {
                      id:1,
                        url:"https://raw.githubusercontent.com/lunnar-being/30questions/master/%E4%B8%80%E4%B8%B2%E7%BA%A2/1.jpg",
                        bounds: [
                            [116.3059,39.9869],[116.4059,39.9869]
                            //22  28
                        ],
                        clickable:true,
                        // events: {
                        //     click(){
                        //         alert('1232131231')
                        //     }
                        // }
                    }
                
        ],
      events:{
        init(o){
          lazyAMapApiLoaderInstance.load().then(()=>{
            _this.initMap()
          })
        }
      }
    };
  },
  
  methods: {
    initMap(){
      this.map=amapManager.getMap();
      // console.log(this.map)
      let marker=new AMap.Marker({
        position:[116.3059, 39.9869],
        content:"<div style='height:20px;width:20px;border-radius:50%;><111></div>"
      });
      marker.setMap(this.map)

      var geolocation=new AMap.Geolocation({
        enableHighAccuracy:true,
        timeout:10000,
        buttonPosition:"RB",
        buttonOffset:new AMap.Pixel(10,20),
        zoomToAccuracy:true,
        markerOptions:{
          content:"11111"
        }
      });
      this.map.addControl(geolocation)
      geolocation.getCurrentPosition(function(status,result){
        if (status=='complete'){
          // onComplete(result)
        }else{
          // onError(result)
        }
      })

      var img1=new AMap.GroundImage({
        url:"https://raw.githubusercontent.com/lunnar-being/30questions/master/%E4%B8%80%E4%B8%B2%E7%BA%A2/1.jpg"
      })
    },
    // point() {
    //   let icon = new AMap.Icon({
    //     image: location,
    //     size: new AMap.Size(2, 2),
    //     imageSize: new AMap.Size(2, 2),
    //   });

    //   let markers = [];
    //   let windows = [];
    //   let that = this;
    //   let pointMaker = [
    //     {
    //       lng:116.3059,
    //       lat:39.9869,
    //       flowerName: "玫瑰花",
    //     },
    //   ];
    //   pointMaker.forEach((item, index) => {
    //     markers.push({
    //       position: [item.lng, item.lat],
    //       icon: location,
    //       events: {
    //         click() {
    //           that.windows.forEach(window => {
    //             window.visible = false;
    //           });
    //           that.window = that.windows[index];
    //           that.$nextTick(() => {
    //             that.window.visible = True;
    //           });
    //         },
    //       },
    //     });
    //     window.push({
    //       position: [item.lng, item.lat],
    //       content: "" + "<div>" + "花名：" + item.flowerName + "</div>",
    //       offset: [5, -15],
    //       visible: false,
    //     });
    //   });
    //   this.markers=markers
    //   this.windows=windows
    // },
  },
  // mounted(){
  //           this.point()
  //       }
};
</script>
<style scope>
.amap-wrapper {
  width: 600px;
  height: 600px;
}
.ant-breadcrumb {
  font-size: 16px;
}

.ant-divider-horizontal {
  margin-top: 16px !important;
  margin-bottom: 16px !important;
}
</style>