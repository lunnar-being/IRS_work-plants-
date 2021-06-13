<template>
  <div>
    <a-breadcrumb separator="">
      <a-breadcrumb-item> 当前位置：检索结果 </a-breadcrumb-item>
    </a-breadcrumb>
    <a-divider></a-divider>
    <div>
      全文检索：
      <a-input-search
        v-model="keyword"
        style="margin-right: 30px; width: 300px"
        placeholder="关键词/花名"
        @search="handleSearchList"
      />
      分类：
      <a-select
        v-model="categoryName"
        default-value="全部"
        style="margin-right: 30px; width: 250px"
        @change="handleCategoryChange"
      >
        <a-select-option
          :key="item"
          v-for="item in catagoryOptions"
          :value="item"
        >
          {{ item }}
        </a-select-option>
      </a-select>
      排序:
      <a-select
        v-model="sort"
        default-value="按出版时间排序"
        style="width: 250px"
        @change="handleSortChange"
      >
        <a-select-option :key="item" v-for="item in sortOptions" :value="item">
          {{ item }}
        </a-select-option>
      </a-select>
    </div>
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
      sortOptions: [
        "按出版时间排序",
        "按销量排序",
        "按价格降序",
        "按价格升序",
        "按相关度排序",
      ],
      catagoryOptions: [
        "全部",
        "医学与生物学",
        "历史与考古",
        "哲学与宗教",
        "商业与经济",
        "地球与环境科学",
        "工程与应用科学",
        "数学、物理与化学",
        "新闻与传播",
        "法律、政治与政府",
        "社会科学",
        "艺术与建筑",
        "语言与文学",
        "音乐、舞蹈、戏剧与电影",
      ],
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
    getList() {
      let keyword = this.keyword;
      let categoryName = this.categoryName;
      let pageNum = this.pageNum - 1;
      let pageSize = 10;
      let sortValue = 1;
      if (this.sort == "按销量排序") {
        sortValue = 2;
      } else if (this.sort == "按价格升序") {
        sortValue = 3;
      } else if (this.sort == "按价格降序") {
        sortValue = 4;
      } else if (this.sort == "按相关度排序") {
        sortValue = 5;
      } else if (this.sort == "按出版时间排序") {
        sortValue = 1;
      }
      searchBooks(keyword, categoryName, pageNum, pageSize, sortValue).then(
        (response) => {
          this.list = response.data.content;
          this.total = response.data.total;
        }
      );
    },
    handleSearchList() {
      this.pageNum = 1;
      this.getList();
    },
    handleCategoryChange(categoryName) {
      this.categoryName = categoryName;
      this.getList();
    },
    handleSortChange(sort) {
      this.sort = sort;
      this.getList();
    },
    handleCurrentChange(pageNum) {
      this.pageNum = pageNum;
      this.getList();
    },
    handleAddCart(e) {
      let bookId = e.currentTarget.id;
      let price =
        e.currentTarget.parentElement.previousElementSibling.previousElementSibling.firstElementChild.innerHTML.substr(
          1
        );
      console.log("entrance1");
      let username = getCookie("username");
      addCart(username, bookId, price).then((response) => {
        this.$message.success({
          content: "加入购物车成功",
          duration: 3,
        });
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

.list {
  margin-top: 15px;
  float: left;
}

.bookList {
  float: left;
}

.bookList ul {
  list-style: none;
  margin: 0px;
}

.bookList li {
  float: left;
  width: 100%;
  border: 1px solid #e9e9e9;
  padding: 20px 30px 20px 20px;
  border-bottom: 1px solid #e9e9e9;
}

.bookList li .info h2 {
  height: 18px;
  overflow: hidden;
  font-weight: normal;
  font-size: 14px;
  line-height: 16px;
}

.bookList li .info .otherInfo {
  margin-top: 6px;
  height: 26px;
  overflow: hidden;
  line-height: 26px;
}

.bookList li .info .priceWrap {
  height: 30px;
  line-height: 30px;
  vertical-align: bottom;
}

.bookList li .info .priceWrap span {
  font-size: 18px;
  color: #e60000;
  margin-right: 10px;
  font-family: "Microsoft YaHei";
}

.bookList li .info .desc {
  line-height: 22px;
  height: 44px;
  overflow: hidden;
  color: #666666;
  margin-top: 10px;
}

.bookList li .info .action {
  overflow: hidden;
  margin-top: 10px;
}

.bookList .cover {
  height: 200px;
  width: 200px;
  float: left;
  display: inline;
  margin-right: 20px;
  text-align: center;
}
</style>