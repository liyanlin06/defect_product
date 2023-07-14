<script >
import { ref } from 'vue'

import axios from "axios";

import { ElMessage, ElMessageBox } from 'element-plus'
export default {
  data() {
    return {
      server_url: "http://127.0.0.1:5000",
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
      is : 0,
      formdata: new FormData(),
      is1: 0,
      rules: {
        email: [
          { required: true, message: '请输入邮箱', trigger: 'blur' },
          { type: 'email', message: '邮箱格式不正确', trigger: ['blur', 'change'] }
        ]
      }
    };


  },



  methods: {

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
       this.is=1;
      this.percentage = 0;

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

      this.formdata.append('files',file);
       this.is1=1;
      //let param =files;
      // var timer = setInterval(() => {
      //   this.myFunc();
      // }, 30);
      let config = {
        headers: { "Content-Type": "multipart/form-data" },
      }; //添加请求头

      axios
          .post(this.server_url + "/upload_zip", this.formdata,)
          .then(response=>{
            if (response.status===200){
              this.is1=1
            }
          })
;

    },
    update1(e) {



      this.$refs.form.validate(valid => {
        if (valid) {
          // 表单验证通过，执行提交操作

          let param = new FormData(); //创建form对象
          param.append("address",this.form.email); //通过append向form对象添加数据



          let config = {
            headers: { "Content-Type": "multipart/form-data" },
          }; //添加请求头

          axios
              .post(this.server_url + "/email", param, config)
              .then(response=>{
                ElMessageBox.alert("结果已发送至您的邮箱")
                this.dialogFormVisible=false
              })
          ;


          console.log('提交表单');
        } else {
          // 表单验证不通过
          console.log('表单验证失败');
        }
      });






    },
    httpRequest(){
      if (this.is1===0){
        ElMessageBox.alert("请先选择文件");
        stop();
      }
      if (this.is1===1){
        this.dialogFormVisible=true;
      }

    },
    uploadsucess(){


        this.is=1
      this.is1=1

    },
    uploaderror(response){
      console.log(response)
    }



  },




}


</script>

<template>



  <el-dialog v-model="dialogFormVisible" title="请输入邮箱:" width="30%" >
    <el-form :model="form" :rules="rules" ref="form">
      <el-form-item label="邮箱地址:" :label-width="formLabelWidth" prop="email">
        <el-input v-model="form.email" autocomplete="off" />

      </el-form-item>

    </el-form>
    <el-button @click="update1">确定</el-button>

  </el-dialog>

  <div class="container">
    <el-card class="card">
      <div class="card-footer" style="width: 100%;">  <el-upload

          action="api/upload_zip"
          :on-success="uploadsucess"
          :on-error="uploaderror"
          accept=".zip"
      >
        <div style="text-align: center;width: 200px" >
          <el-button  type="primary"  >文件上传</el-button>
        </div>




      </el-upload>
      </div>
    </el-card>

    <el-card class="card">
      <div class="card-footer">
        <el-button @click="httpRequest()" v-if="this.is===1">输入邮箱</el-button>
      </div>

    </el-card>
  </div>




</template>

<style scoped>

.container {
  display: flex;
  flex-direction: column;  /* 竖直方向排列 */
  width: 100%;
  justify-content: center;
}

.card {
  margin-bottom: 20px;  /* 设置卡片之间的间距 */
  height: 150px;

}

.card .card-footer {
  display: flex;
  justify-content: center;
  width: 100%;
}

</style>
