<template>
  <div>
    <el-main class="content1">
      <div class="search_box">
        <div class="our_name">
          <img
            src="../../src/image/shumiao.png"
            style="height: 25px; width: 25px"
          />
          &nbsp; 燕园草木识别与检索系统
        </div>
        <div class="bar1">
          <form>
            <input
              type="text"
              placeholder="请输入您要搜索的内容..."
              v-model="keywords"
            />
            <button type="submit" @click="submit_key">
              <img
                src="../../src/image/sousuo.png"
                style="height: 25px; width: 25px"
              />
            </button>
          </form>
        </div>
      </div>
    </el-main>
    
  </div>
</template>

<script>
export default {
  data() {
    return {
      keywords: "",
      
    };
  },
  methods: {
    submit_key() {
      console.log(this.keywords);
      this.$router.push('result')
    },
  },
};
</script>
<style>
.header {
  margin-bottom: 0 !important;
}
.content1 {
  margin-top: 0 !important;
  width: 120% !important;
  position:relative;
  top:-50px;
  left:-110px
}
.el-main {
  background-image: url("../../src/image/bg.png");
  background-repeat: no-repeat;
  background-size: 100% 100%;
  background-position: center center;
  background-attachment: fixed;
  color: #333;
  text-align: center;
  height: 750px;
  margin-top: 0 !important;
  vertical-align: middle;
}
.search_box {
  width: 1000px;
  border: 2px solid #62ab8a;
  border-radius: 5px;
  margin: 0 auto;
  position: relative;
  top: 20%;
}
.our_name {
  color: #ffffff;
  font-size: 24px;
  font-weight: 600;
  background-color: #a3d0c3;
  padding-top: 10px;
}
form {
  position: relative;
  width: 700px;
  height: 200px;
  margin: 0 auto;
}
input,
button {
  border: none;
  outline: none;
}
.bar1 {
  background: #a3d0c3;
}
.bar1 input {
  border: 2px solid #7ba7ab;
  border-radius: 5px;
  color: #9e9c9c;
  width: 100%;
  height: 50px;
  padding-left: 13px;
  margin-top: 50px;
}
.bar1 button {
  top: 0;
  right: 0;
  background: #7ba7ab;
  border-radius: 0 5px 5px 0;
  height: 50px;
  width: 50px;
  cursor: pointer;
  position: absolute;
  margin-top: 50px;
}
</style>





  
  

