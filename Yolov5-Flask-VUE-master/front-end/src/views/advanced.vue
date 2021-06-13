<template>
  <div>
    <a-breadcrumb separator="">
      <a-breadcrumb-item> 当前位置：高级检索 </a-breadcrumb-item>
    </a-breadcrumb>
    <a-divider></a-divider>
    <a-form-model
    ref="dynamicValidateForm"
    :model="dynamicValidateForm"
    v-bind="formItemLayoutWithOutLabel"
  >
    <a-form-model-item
      v-for="(domain, index) in dynamicValidateForm.domains"
      :key="domain.key"
      v-bind="index === 0 ? formItemLayout : {}"
      :label="index === 0 ? 'Domains' : ''"
      :prop="'domains.' + index + '.value'"
      :rules="{
        required: true,
        message: 'domain can not be null',
        trigger: 'blur',
      }"
    >  
      <a-form-model-item label="逻辑符" v-if="domain.flag">
      <a-select  v-model="domain.region" placeholder="and">
        <a-select-option value="and">
          and
        </a-select-option>
        <a-select-option value="or">
          or
        </a-select-option>
        <a-select-option value="not">
          not
        </a-select-option>
      </a-select>
    </a-form-model-item>
    <div class="input_div">
      <a-input
        v-model="domain.value"
        placeholder="检索词"
        style="width: 60%; margin-left: 8px;margin-top:4px"
      />
      <a-icon
        v-if="dynamicValidateForm.domains.length > 1"
        class="dynamic-delete-button"
        type="minus-circle-o"
        :disabled="dynamicValidateForm.domains.length === 1"
        @click="removeDomain(domain)"
      />
      </div>
    </a-form-model-item>
    <a-form-model-item v-bind="formItemLayoutWithOutLabel">
      <a-button type="dashed" style="width: 60%" @click="addDomain">
        <a-icon type="plus" /> Add field
      </a-button>
    </a-form-model-item>
    <a-form-model-item v-bind="formItemLayoutWithOutLabel">
      <a-button type="primary" html-type="submit" @click="submitForm('dynamicValidateForm')">
        Submit
      </a-button>
      <a-button style="margin-left: 10px" @click="resetForm('dynamicValidateForm')">
        Reset
      </a-button>
    </a-form-model-item>
  </a-form-model>
    <a-divider>检索结果</a-divider>
    <a-list
      item-layout="vertical"
      size="large"
      :pagination="pagination"
      :data-source="listData"
    >
      <div slot="footer"><b>ant design vue</b> footer part</div>
      <a-list-item slot="renderItem" key="item.title" slot-scope="item">
        <template v-for="{ type, text } in actions" slot="actions">
          <span :key="type">
            <a-icon :type="type" style="margin-right: 8px" />
            {{ text }}
          </span>
        </template>
        <img
          slot="extra"
          width="272"
          alt="logo"
          src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
        />
        <a-list-item-meta :description="item.description">
          <a slot="title" :href="item.href">{{ item.title }}</a>
          <a-avatar slot="avatar" :src="item.avatar" />
        </a-list-item-meta>
        {{ item.content }}
      </a-list-item>
    </a-list>
  </div>
</template>
<script>
// import { formatDate } from '@/utils/date.js'
// import { searchBooks, addCart } from '@/api/index.js'
// import { getCookie } from '@/utils/support'
const listData = [];
for (let i = 0; i < 23; i++) {
  listData.push({
    href: 'https://www.antdv.com/',
    title: `ant design vue part ${i}`,
    avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    description:
      'Ant Design, a design language for background applications, is refined by Ant UED Team.',
    content:
      'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
  });
}
export default {
  data() {
    return {
      keyword: "",
      categoryName: "全部",
      sort: "按出版时间排序",
      
      pageNum: 1,
      total: 1,
      listData,
      pagination: {
        onChange: page => {
          console.log(page);
        },
        pageSize: 3,
      },
      actions: [
        { type: 'star-o', text: '156' },
        { type: 'like-o', text: '156' },
        { type: 'message', text: '2' },
      ],
      formItemLayout: {
        labelCol: {
          xs: { span: 24 },
          sm: { span: 4 },
        },
        wrapperCol: {
          xs: { span: 24 },
          sm: { span: 20 },
        },
      },
      formItemLayoutWithOutLabel: {
        wrapperCol: {
          xs: { span: 24, offset: 0 },
          sm: { span: 20, offset: 4 },
        },
      },
      dynamicValidateForm: {
        domains: [
          {
            region:undefined,
            key:1,
            flag:false,
            value:''
          }
        ],
      },
    };
  },
  filters: {
    formatTime(time) {
      let date = new Date(time);
      return formatDate(date, "yyyy-MM-dd");
    },
  },
  created() {
    this.getList();
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          alert('submit!');
          console.log(this.dynamicValidateForm.domains)
          this.axios.post('http://127.0.0.1:5000/advanced',JSON.stringify(this.dynamicValidateForm.domains)).then((body)=>{
            console.log(body.data)
          });
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    removeDomain(item) {
      let index = this.dynamicValidateForm.domains.indexOf(item);
      if (index !== -1) {
        this.dynamicValidateForm.domains.splice(index, 1);
      }
    },
    addDomain() {
      this.dynamicValidateForm.domains.push({
        value: '',
        key: Date.now(),
        flag:true,
        region:undefined
      });
    },
  },
};
</script>
<style scope>
.ant-breadcrumb {
  font-size: 16px;
}
.ant-divider-inner-text{
    color:#44ae88;
    font-size: 20px;
    font-weight: bold;
}
.ant-divider-horizontal {
  margin-top: 16px !important;
  margin-bottom: 16px !important;
}

.dynamic-delete-button {
  cursor: pointer;
  position: relative;
  top: 4px;
  font-size: 24px;
  color: #999;
  transition: all 0.3s;
}
.dynamic-delete-button:hover {
  color: #777;
}
.dynamic-delete-button[disabled] {
  cursor: not-allowed;
  opacity: 0.5;
}
.ant-form-item-children{
  /* width:40%; */
  display: flex;
  justify-content:flex-start;
}
.input_div{
  width:200px;
  height: 30px;
  margin-top: 34px;
}
.ant-col .ant-form-item-control-wrapper{
  width: 60px;
  position: relative;
  right:0px
}
.ant-select .ant-select-enabled{
  width:60px
}
/* body > div.index > section > main > section > div > form > div:nth-child(1) > div.ant-col.ant-col-xs-24.ant-col-sm-20.ant-form-item-control-wrapper > div > span > div.ant-row.ant-form-item > div.ant-col.ant-form-item-control-wrapper > div > span{
  width:60px
} */
.ant-select .ant-select-enabled{
  width: 60px;
}
.ant-form-item{
  margin-bottom: 5px;
}
body > div > section > main > section > div > form > div:nth-child(1) > div.ant-col.ant-col-xs-24.ant-col-sm-20.ant-form-item-control-wrapper > div > span > div{
  margin-left: 60px;
}
</style>