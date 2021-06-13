<template>
  <div>
    <a-breadcrumb separator="">
      <a-breadcrumb-item>
        <router-link to="/store/index">当前位置：首页</router-link>
      </a-breadcrumb-item>
      <a-breadcrumb-separator>></a-breadcrumb-separator>
      <a-breadcrumb-item> 图像上传 </a-breadcrumb-item>
    </a-breadcrumb>
    <a-divider></a-divider>
    <div class="clearfix">
    <a-upload
      :customRequest='addImage'
      list-type="picture-card"
      :headers="{'Authorization':token}"
      :file-list="fileList"
      @preview="handlePreview"
      @change="handleChange"
    >
      <div v-if="fileList.length < 8">
        <a-icon type="plus" />
        <div class="ant-upload-text">
          Upload
        </div>
      </div>
    </a-upload>
    <a-modal :visible="previewVisible" :footer="null" @cancel="handleCancel">
      <img alt="example" style="width: 100%" :src="previewImage" />
    </a-modal>
    <a-list
      item-layout="vertical"
      size="large"
      :pagination="pagination"
      :data-source="listData"
    >
      <!-- <div slot="footer"><b>燕园草木</b> footer part</div> -->
      <a-list-item slot="renderItem" key="item.id" slot-scope="item">
        <!-- <template v-for="{ type, text } in actions" slot="actions">s
          <span :key="type">
            <a-icon :type="type" style="margin-right: 8px" />
            {{ text }}
          </span>
        </template> -->
        <img
          slot="extra"
          width="272"
          alt="logo"
          :src="item.img"
        />
        <a-list-item-meta :cat="item.cat">
          <a slot="title" :href="item.href" style="font-weight:bold">{{ item.name_ch }}</a>
          <a-avatar slot="avatar" :src="item.img" />
        </a-list-item-meta>
        <p ><span style="font-weight:bold;color:#44ae88">生物学分类</span>：{{item.cat}}</p>
        <span style="font-weight:bold;color:#44ae88">植物信息：</span>{{ item.content}}
        <a style='color:#44ae88;font-weight:bold'><router-link to="/detail">更多信息</router-link></a>
      </a-list-item>
    </a-list>
    <!-- <a-result title="Great, we have done all the operations!">
    <template #icon>
      <a-icon type="smile" theme="twoTone" />
    </template>
    <template #extra>
      <a-button type="primary">
        查看具体信息
      </a-button>
    </template>
  </a-result> -->

  </div>
  </div>
</template>
<script>
function getBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = error => reject(error);
  });
}
export default {
  data() {
    return {
      previewVisible: false,
      previewImage: '',
      pageNum: 1,
      total: 1,
      listData:[],
      pagination: {
        onChange: (page) => {
          console.log(page);
        },
        pageSize: 3,
      },
      actions: [
        { type: "star-o", text: "156" },
        { type: "like-o", text: "156" },
        { type: "message", text: "2" },
      ],
      url:'http://127.0.0.1:5000/image',
      fileList: [
        {
          uid: '-1',
          name: 'image.png',
          status: 'done',
          url: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
        },
      ],
    };
    
  },
  methods: {
    handleCancel() {
      this.previewVisible = false;
    },
    async handlePreview(file) {
      if (!file.url && !file.preview) {
        file.preview = await getBase64(file.originFileObj);
      }
      this.previewImage = file.url || file.preview;
      this.previewVisible = true;
    },
    handleChange({fileList}) {
        // console.log(e)
        // let file = e.target.file[0];
        // let param = new FormData();
        // param.append('file',file);
        // let config={
        //     headers:{'Content-Type':'multipart/form-data'}
        // };
        // axios.post('http://127.0.0.1:5000/image',param,config).then(response=>{
        //     console.log(response.data);
        // })
      this.fileList = fileList;
    },
    addImage(data){
      let formdata=new FormData();
      formdata.append('file',data.file);
      console.log(formdata.get('file'));
      let config={
        headers:{'Content-Type':'multipart/form-data'}
      }
      this.axios.post('http://127.0.0.1:5000/image',formdata,config).then(response=>{
        console.log(response)
        console.log(response.status)
        if (response.status==200){
          data.onSuccess(response.data);
          console.log(this.fileList)
          this.fileList[this.fileList.length-1].status='done'
          this.listData=response.data
          console.log(response.data)
        }else{
          data.onError();
        }
      })
    }
  },
};
</script>
<style scope>
.ant-breadcrumb {
  font-size: 16px;
}

.ant-divider-horizontal {
  margin-top: 16px !important;
  margin-bottom: 16px !important;
}
.ant-upload-select-picture-card i {
  font-size: 32px;
  color: #999;
}

.ant-upload-select-picture-card .ant-upload-text {
  margin-top: 8px;
  color: #666;
}
</style>