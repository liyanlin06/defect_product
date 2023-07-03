// const { VertexBuffer } = require("XrFrame/kanata/lib/index");

var app = getApp()  
Page({  
  data: {  //下面的数据是设置全局变量
    tempFilePaths: '',
    result:'',
    pre_time:'',
    detect_time:'',
    cloudPath:'',
    listResult:'',
    
  },  
  onLoad:function(options){
      this.chooseimage_cloud
  },
  chooseimage_cloud: function () {  
    var fileid_id = ''
    var _this = this;  
    // var random_1 = Math.floor(Math.random() * 10);//生成0-10的数字,随机确定百位
    // var random_2 = Math.floor(Math.random() * 100);//生成0-100的数字,随机确定十位和个位

    // var random_1_1 = Math.floor(Math.random() * 10);//生成0-10的数字,随机确定百位
    // var random_2_2 = Math.floor(Math.random() * 100);//生成0-100的数字,随机确定十位和个位



    // var random_time = random_1*100+random_2;//生成一个三位整数
    // var random_time_pre = random_1_1*100+random_2_2;//生成一个三位整数
    // var random_3 = Math.floor(Math.random() + 0.5);//小于一和大于一的概率都是0.5
    // var random_4 = Math.floor(Math.random() + 0.5);//小于一和大于一的概率都是0.5
    // var random_result = '未知'
    // var random_type = '未知类别'
    // if (random_3>=1)
    //   random_result = '有缺陷';
    // else
    //   random_result = '无缺陷';
    
    // if (random_4>=1)
    //   random_type = '随机类别一';
    // else
    //   random_type = '随即类别二';

    wx.chooseMedia({  
      count: 1, //指定最多上传图片的大小
      mediaType: ['image'],
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有  
      sizeType: ['original'],
      camera: 'back',
      success: function (res) {  
        const tempFilePaths = res.tempFiles
        console.log('===================tempFiles = ',tempFilePaths)
        const filePath = String(res.tempFiles[0].tempFilePath)
        const cloudPath = 'WX.image'

        _this.setData({  
          //这里设置在前端展示的内容,第一个是是否有缺陷,第二个是处理速度  
          tempFilePaths:res.tempFiles[0].tempFilePath 
        })  
        wx.showLoading({
          title: '正在上传请稍后',
          mask:true
        })

        wx.uploadFile({
         
          filePath: _this.data.tempFilePaths,
          name: 'file',
          // 服务器地址等后端部署到服务器上之后需要更改
          url: 'http://127.0.0.1:5000/upload',//服务器地址
          header:{'Content-Type':'application/json'},
          success: (res2) => {   //成功之后执行的方法
              
              console.log(res2.data)
              var obj=JSON.parse(res2.data);
              var result=obj.result;
              var time=obj.time

              _this.setData({
                listResult:result,
                listTime:time
                })
              wx.hideLoading({ //隐藏加载框
              }).then(res2 => {
                wx.showToast({ //提示框
                  title: '上传成功',
                  duration:2000,
                  success:function(){
                   
                    // var that=this;
                    // wx.request({
                      
                    //   url: 'http://127.0.0.1:5000/upload',
                    //   data:{},
                    //   method:"GET",
                    //   header:{ 
                    //     'content-type':'application/json'
                    //   },
                    //  success:function(res){



                    //   }
                    // })


                


                  }
                })
              
          })
        },
          fail: res => {
          wx.hideLoading({ //隐藏加载框
          }).then(res => {
            wx.showModal({
              title: '请求失败',
              content: "请检查服务器连接"
            })
          })
        }

          })
     
      }
    })
  },

      // 发起POST请求
      postInfo() {
        var _this = this;  
        var random_1 = Math.floor(Math.random() * 10);//生成0-10的数字,随机确定百位
        var random_2 = Math.floor(Math.random() * 100);//生成0-100的数字,随机确定十位和个位
        var random_time = random_1*100+random_2;
        var random_3 = Math.floor(Math.random() + 0.5);//小于一和大于一的概率都是0.5
        var random_4 = Math.floor(Math.random() + 0.5);//小于一和大于一的概率都是0.5
        var random_result = '未知'
        var random_type = '未知类别'
        if (random_3>=1)
          random_result = '有缺陷';
        else
          random_result = '无缺陷';
        
        if (random_4>=1)
          random_type = '随机类别一';
        else
          random_type = '随即类别二';




        wx.request({
        url: 'https://www.escook.cn/api/post',
        // url:'https://t54897w513.goho.co/',
        method: "POST",
        data: {
            result: random_result,
            time: random_time,
            type: random_type
        },
        success: (res) => {
            console.log(res)
            console.log(res.data)

            // console.log(res.data.data.age)
            // console.log(res.data.age)
            // console.log(res.data.time)
        }
        })
    }

})  
//   // 上传图片到服务器
// //   upload() {
// //     var _this=this
// //     wx.chooseMedia()({
// //         count: 1,   //可上传的图片数量
// //         sizeType: ['original', 'compressed'],//上传图片类型：原图、压缩图
// //         sourceType: ['album', 'camera'], //图片来源：相册、照相机
// //         success(res) {
// //             // 成功，将图片上传到服务器
// //             console.log(res);
// //             // 拿取临时路径文件
// //             let filePath = res.tempFilePaths[0]
// //             /*  
// //              控制台的 tempFilePaths: ["http://tmp/DTalF29Fe4wkc6221b571e512fe6b7a68b2926e81b51.jpg"]
// //               即表示图片的临时路径
// //            */
// //             wx.uploadFile({
// //                 /* // 拿到临时图片路径后上传到服务器，服务器将返回一个公网地址，
// //                 届时在任意角落都将能访问到这张图片 */
// //                 filePath: filePath, //临时文件路径
// //                 url: baseUrl + "/api/test/user/upload",  //填写公司的服务器地址
// //                 name: 'file',   /* //非常重要！！！！是后台访问二进制数据的关键 
// //                 该 file 是对应接口，所需要传递的参数 */
// //                 timeout:5000,
// //                 success(res2){
// //                     console.log(res2);
// //                     // 需解析信息，拿到图片路径，因为本项目的 域名以 .com 结尾，所以需要“ / ”进行必要分隔
// //                     let imgPath=baseUrl+"/"+JSON.parse(res2.data).data //将二进制转换成字符串类型
// //                     _this.setData({
// //                         imgPath
// //                     })

// //                 }
// //             })
// //         }
// //     })
// // },
//   onLoad: function () {  
//   },  
//   detect: function () {  
//     var _this = this;  //通过this这个实例来调用接口
//     var random_1 = Math.floor(Math.random() * 10);//生成0-10的数字,随机确定百位
//     var random_2 = Math.floor(Math.random() * 100);//生成0-100的数字,随机确定十位和个位

//     var random_1_1 = Math.floor(Math.random() * 10);//生成0-10的数字,随机确定百位
//     var random_2_2 = Math.floor(Math.random() * 100);//生成0-100的数字,随机确定十位和个位



//     var random_time = random_1*100+random_2;//生成一个三位整数
//     var random_time_pre = random_1_1*100+random_2_2;//生成一个三位整数
//     var random_3 = Math.floor(Math.random() + 0.5);//小于一和大于一的概率都是0.5
//     var random_4 = Math.floor(Math.random() + 0.5);//小于一和大于一的概率都是0.5
//     var random_result = '未知'
//     var random_type = '未知类别'
//     if (random_3>=1)
//       random_result = '有缺陷';
//     else
//       random_result = '无缺陷';
    
//     if (random_4>=1)
//       random_type = '随机类别一';
//     else
//       random_type = '随即类别二';

//     wx.chooseMedia({  
//       count: 1, //指定最多上传图片的大小
//       mediaType: ['image'],//指定上传的文件类型为图片类型
//       sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有  
//       sizeType: ['original'],//这是原图的意思，另外有一个压缩的选项，我们默认原图，方便检测
//       camera: 'back',//如果要拍照的话，默认设置为后置摄像头
//       success: function (res) {  
//         // 返回选定照片的本地文件路径列表,tempFiles[i]里面包含某张图片信息,如下 
//         // 3个值：fileType:"image";size:大小;tempFilePath:路径
//         // [i]可以选择第几张图片,如果想要发送所有图片的话使用for循环即可
//         // 但是为了方便开发,我决定选择一次只能选择一张图片来进行,多图片交给WEB端
//         console.log(res.tempFiles)//console.log()函数是在控制台进行打印,res是返回值,tempFiles是本地文件信息，包括路径，大小，多少张之类的信息
//         console.log(res.tempFiles[0].tempFilePath)//第一张图片的本地路径（因为可以选择多张，所以是数组类型）
//         _this.setData({  
//           tempFilePaths:res.tempFiles[0].tempFilePath//这里的setData方法是设置前端的绑定值，与VUE语法类似，先空着，拿到数据后再让前端显示出来  
//         })  

//         wx.uploadFile({
//           filePath: tempFilePaths,
//           name: 'name',//接口
//           url: 'url',//服务器地址
//           success: (res2) => {   //成功之后执行的方法
//               console.log(res2)
//               let imgPath=baseUrl+"/"+JSON.parse(res2.data).data //将二进制转换成字符串类型
//               _this.setData({
//                   imgPath
//               })
//           }
//           })
//       }  
//     })  
//   },

//  previewImg: function (e) {
//      //获取当前图片的下标
//     var index = e.currentTarget.dataset.index;
//      //所有图片
//     var imgs = this.data.imgs;

//     wx.previewImage({
//       //当前显示图片
//       current: imgs[index],
//       //所有图片
//       urls: imgs
//     })},

    // wx.cloud.uploadFile({
        //   cloudPath:cloudPath,    //这里的cloudPath是云端服务器的id，通过id来传到对应的服务器上
        //   // url: 'http://example.weixin.qq.com/upload', //仅为示例，非真实的接口地址
        //   // url:'https://t54897w513.goho.co/',
        //   filePath: filePath,
        //   name: 'JPG',
        //   formData:{
        //     'user': 'WECHAT-YZQ'    //额外携带的数据
        //   },
        //   success: function(res){   //上传成功后执行的代码
        //     console.log('OK')
        //     console.log('云端ID为:'+res.fileID)
        //     var data = JSON.parse(res.data)
        //     console.log(data)
        //     //do something
        //     fileid_id = res.fileID
        //     console.log()
        //   },
        //   complete: function (res) {  //无论成功与否，都会执行的方法
        //     console.log('方法完成了,自动执行现在的部分');
        //     console.log('这是在打印fileid之前的句子')
        //     console.log(res.fileID)
        //     console.log(fileid_id)
        //     wx.cloud.getTempFileURL({   //微信小程序的接口，用于获取下载链接
        //       fileList: [{
        //         fileID: res.fileID,     //通过文件id来查找文件
        //         maxAge: 60 * 60, // one hour，也就是这个文件的存活时间，超过这个时间就不要了
        //       }]
        //     }).then(res => {
        //       // get temp file URL
        //       console.log('现在进入到了指定位置')
        //       console.log(res.fileList)
        //       var URL = res.fileList[0].tempFileURL
        //       // wx.request({
        //       //   // url: 'https://www.escook.cn/api/post',
        //       //   url:'https://t54897w513.goho.co',
        //       //   method: "POST",
        //       //   data: {
        //       //     downloadURL:URL
        //       //   },
        //       //   // success: (res) => {
        //       //   //     console.log(res)
        //       //   //     console.log('成功了!')
        //       //   //     _this.setData({  
        //       //   //       //这里设置在前端展示的内容,第一个是是否有缺陷,第二个是处理速度  
        //       //   //       // cloudPath:'https://t54897w513.goho.co/image',
        //       //   //       result: res.data.msg,
        //       //   //       pre_time: res.data.time[0],
        //       //   //       detect_time:res.data.time[1]
        //       //   //     })

        //       //   // }
        //       //   })

        //     }).catch(error => {
        //       console.log('发生未知错误')
        //       console.log(error)
        //       // handle error
        //     })
    
        //   }
        // })