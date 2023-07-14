<script >
import { ref } from 'vue'

import axios from "axios";
import { ElMessage } from 'element-plus'
import {result} from "lodash-es";
export default {
  data() {
    return {
      server_url: "http://10.27.202.195:5000",
      activeName: "first",
      active: 0,
      centerDialogVisible: true,
      url_1: "",
      url_2: "",
      textarea: "",
      srcList: [],
      srcList1: [],
      feature_list: [],
      feature_list_1: [],
      feat_list: [],
      url: "",
      visible: false,
      wait_return: "等待上传",
      wait_upload: "等待上传",
      loading: false,
      table: false,
      isNav: false,
      showbutton: true,
      percentage: 0,
      fullscreenLoading: false,
      opacitys: {
        opacity: 0,
      },
      dialogTableVisible: false,
      dialogFormVisible:false,
      form:{},

      imageUrl:null
    };
  },

  created() {
    console.log("")
  },

  methods: {
    result,

    getObjectURL(file) {
      var url = null;
      if (window.createObjcectURL != undefined) {
        url = window.createOjcectURL(file);
      } else if (window.URL != undefined) {
        url = window.URL.createObjectURL(file);
      } else if (window.webkitURL != undefined) {
        url = window.webkitURL.createObjectURL(file);
      }
      return url;
    },
    update(e) {

      this.percentage = 0;
      this.dialogTableVisible = true;
      this.url_1 = "";
      this.url_2 = "";
      this.srcList = [];
      this.srcList1 = [];
      this.wait_return = "";
      this.wait_upload = "";
      this.feature_list = [];
      this.feat_list = [];
      this.fullscreenLoading = true;
      this.loading = true;
      this.showbutton = false;
      let file = e.target.files[0];
      this.url_1 = this.$options.methods.getObjectURL(file);
      //let param = new FormData(); //创建form对象
      //param.append("file", file, file.name); //通过append向form对象添加数据
      let param =file;
      var timer = setInterval(() => {
        this.myFunc();
      }, 30);
      let config = {
        headers: { "Content-Type": "multipart/form-data" },
      }; //添加请求头

      axios
          .post(this.server_url + "/upload", param, config)
          .then((response) => {
            this.percentage = 100;
            clearInterval(timer);
            this.url_1 = response.data.image_url;
            this.srcList.push(this.url_1);
            this.url_2 = response.data.draw_url;
            this.srcList1.push(this.url_2);
            this.fullscreenLoading = false;
            this.loading = false;

            this.feat_list = Object.keys(response.data.image_info);

            for (var i = 0; i < this.feat_list.length; i++) {
              response.data.image_info[this.feat_list[i]][2] = this.feat_list[i];
              this.feature_list.push(response.data.image_info[this.feat_list[i]]);
            }

            this.feature_list.push(response.data.image_info);
            this.feature_list_1 = this.feature_list[0];
            this.dialogTableVisible = false;
            this.percentage = 0;
            this.notice1();
          });
    },
    update1(e) {
      let param = new FormData(); //创建form对象
      param.append("address",form.email); //通过append向form对象添加数据


      let config = {
        headers: { "Content-Type": "multipart/form-data" },
      }; //添加请求头

      axios
          .post(this.server_url + "/email", param, config)
          .then(response => {
            const responseData = response.data
            console.log(responseData)
          })
      ;
    },



    FilesUploadSuccess(response) {
      console.log(response)
      // 在这里获取后端返回的JSON数据
      // 在这里对responseData进行处理
      let rs1={
        class:response.result,
        time:response.time,
        con:response.con
      }
      console.log(rs1)
      this.feature_list.push(rs1)
    },


    handleFileChange(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.imageUrl = e.target.result; // 使用FileReader读取文件并生成图片链接
      };
      reader.readAsDataURL(file.raw); // 读取文件内容
    },
  },

}


</script>

<template>
  <div class="container">



  <el-card class="card" >
    <div class="upload" style="text-align: center">

    <el-upload
      action="api/upload"
      :on-success="FilesUploadSuccess"
      @change="handleFileChange"
      accept="image/*"
  >

    <el-button type="primary" >图片上传</el-button>
  </el-upload>
    </div>
  </el-card>

  <el-card class="card" style="height: 250px">
    <div class="image">


    <img :src="imageUrl" alt="Selected Image" v-if="imageUrl" class="card-image"/>
  </div>
  </el-card>





  <el-card class="card">
    <div class="table">
    <el-tabs v-model="activeName">
      <el-table
          :data="feature_list"
          border
          style="width: 750px;"
          v-loading="loading"
          element-loading-text="数据正在处理中，请耐心等待"
          element-loading-spinner="el-icon-loading"
          lazy
      >
        <el-table-column label="目标类别" width="250px" height="50px" prop="class" >
        </el-table-column>

        <el-table-column label="推理时间" width="250px" height="50px" prop="time" >
        </el-table-column>

        <el-table-column label="置信度" width="250px" height="50px" prop="con" >
        </el-table-column>
      </el-table>

    </el-tabs>

    </div>
  </el-card>



  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;  /* 竖直方向排列 */
}

.card {
  margin-bottom: 20px;  /* 设置卡片之间的间距 */

}
.table {
  display: flex;
  justify-content: center; /* 水平方向居中 */
  align-items: center; /* 垂直方向居中 */
}
.image {
  display: flex;
  justify-content: center; /* 水平方向居中 */
  align-items: center; /* 垂直方向居中 */
}
.card-image{
  height: 15%;
  width: 15%;
  object-fit: contain;
}
</style>
