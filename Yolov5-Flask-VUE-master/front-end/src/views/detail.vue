<template>
    <el-container>
        
        <el-header>
          <div style="overflow:hidden;display: inline-block;width: 1050px;height: 60px;">
            <div class=logo>
              <img src='../../src/image/shumiao.png' style="height: 25px;width: 25px;">
              &nbsp;燕园草木识别检索系统
            </div>
            <div class=nav >
              <router-link to="/home">首页</router-link>
              </div>
            <div class=nav >
              <router-link to="/store/contact">联系我们</router-link>
              </div>
          </div>
        </el-header>
        <el-main>
            <div class=box>
                <div class=box_left>
                    <div class=card style="margin-bottom: 25px;height:460px">
                      <div class=card_title>图片</div>
                        <div class="demo-image__preview" style="height:360px">
                            <el-image 
                              style="width: 350px; height: 350px;"
                              :src="url" 
                              :preview-src-list="srcList">
                            </el-image>
                        </div>
                        <div style="height:30px;line-height:30px">
                            点击查看更多预览大图～
                        </div>
                    </div>
                    
                    <div class=card style="margin-bottom: 50px;height:380px">
                        
                            <div class=card_title>Tag</div>
                            <div style="line-height:30px;text-align: left;padding-left: 20px;margin-bottom: 20px;">
                                <el-tag style="margin-right: 10px;margin-bottom:10px ;">标签一</el-tag>
                                <el-tag style="margin-right: 10px;margin-bottom:10px ;">标签一</el-tag>
                                <el-tag style="margin-right: 10px;margin-bottom:10px ;">标签一</el-tag>
                                <el-tag style="margin-right: 10px;margin-bottom:10px ;">标签一</el-tag>
                                <el-tag style="margin-right: 10px;margin-bottom:10px ;">标签一</el-tag>
                                <el-tag style="margin-right: 10px;margin-bottom:10px ;">标签一</el-tag>
                                <el-tag style="margin-right: 10px;margin-bottom:10px ;">标签一</el-tag>
                            </div>
                        
                    </div>
                </div>
                <div class=box_right>
                    <div class=card style="margin-bottom: 50px;">
                        <div class=card_title>基本信息</div>
                        <div>
                            <div style="height:30px;line-height:30px;text-align: left;padding-left: 30px;padding-top: 10px;margin-bottom: 20px;">LatinName / 中文名:</div>
                            <div style="height:30px;line-height:30px;text-align: left;padding-left: 30px;padding-top: 10px;margin-bottom: 20px;">Genus / 属:</div>
                            <div style="height:30px;line-height:30px;text-align: left;padding-left: 30px;padding-top: 10px;margin-bottom: 20px;">Family / 科:</div>
                            <div style="height:30px;line-height:30px;text-align: left;padding-left: 30px;padding-top: 10px;margin-bottom: 20px;">Order / 目:</div>
                            <div style="height:30px;line-height:30px;text-align: left;padding-left: 30px;padding-top: 10px;margin-bottom: 20px;">Class / 纲:</div>
                            <div style="height:30px;line-height:30px;text-align: left;padding-left: 30px;padding-top: 10px;margin-bottom: 20px;">Phylum / 门:</div>
                        </div>
                        <div class=card_title>花木介绍</div>
                        <div style="height:200px;line-height:30px;text-align: left;padding-left: 30px;padding-top: 10px;margin-bottom: 20px;">唧唧呱呱噜噜啦啦这是一段介绍哦</div>
                        <div class=card_title>校内分布</div>
                        <div style="height:30px; line-height:30px;text-align: left;padding-left: 30px;padding-top: 10px;margin-bottom: 20px;">唧唧呱呱噜噜啦啦这是一段介绍哦</div>
                    </div>
                    
                </div>
            </div>
        </el-main>
        <el-footer>Copyright © 2021 燕园草木识别检索系统小组  All Rights Reserved.</el-footer>
      </el-container>
</template>

<style>
  .el-header{
    background-color: #74b4a7;
    color: #333;
    text-align: center;
    line-height: 60px;
    height: 60px !important;
    width: 100%;
    position: fixed;
    z-index: 1;
    }
  .el-footer{
    background-color: #364b6b;
    color: #333;
    text-align: center;
    line-height: 60px;
    color: white;
  }
  .el-main {
    background-image: url('../../src/image/bg.png');
    background-repeat: no-repeat;
    background-size:100% 100% ; 
    background-position: center center;
    background-attachment: fixed;
    color: #333;
    text-align: center;
    margin-top: 54px;
  }
  .box{
      overflow:hidden;
      display: inline-block;
      padding: 20px;
      background-color: rgba(255,255,255,0.6);
  }
  .box_left{
      width:400px;
      margin-right: 25px;
      float:left;
  }
  .box_right{
      width:600px;
      float:left;
  }
  .card{
    border: 1px solid #EBEEF5;
    background-color: #FFF;
    color: #303133;
    box-shadow: 0 2px 12px 0 rgb(0 0 0 / 10%)
}
  .card_title{
    height:40px;line-height:40px;font-size:20px;text-align: left;color:white;padding-left: 20px;margin-bottom: 20px;background-color: #74b4a7;
  }
  .logo{
    width:300px;
    height: 60px;
    margin-right: 20px;
    float:left;
    font-size: 20px;
    color: white;
  }
  .nav{
    height:60px;
    width: 100px;
    margin-right: 20px;
    float:right;
    font-size: 20px;
    color: white;
  }

</style>

<script>
    export default {
    data() {
      return {
        url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        srcList: [
          'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
          'https://fuss10.elemecdn.com/1/8e/aeffeb4de74e2fde4bd74fc7b4486jpeg.jpeg'
        ]
      }
    }
  }
</script>
