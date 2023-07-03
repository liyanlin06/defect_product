// pages/home/home.js
Page({

  data: {

  },
  onLoad: function (options) {
    //查看是否授权
    wx.getSetting({
      success: function(res) {
        if (res.authSetting['scope.userInfo']) {
          console.log("用户授权了");
        } else {
          //用户没有授权
          console.log("用户没有授权");
        }
      }
    });
},

  index:function(){
    wx.getUserProfile({
      desc: '用于微信账号与平台账号绑定', 
      success: (res)=>{
        wx.navigateTo({
     
          url: '/pages/index/index',
         
        })
        console.log("获取到的用户信息成功: ",JSON.stringify(res));
        this.setData({
          userInfo: res,
          userInfoStr: JSON.stringify(res)
        })
      },
      fail: (res)=>{
        console.log("获取用户个人信息失败: ",res);
         //用户按了拒绝按钮
               wx.showModal({
                  title: '警告',
                  content: '您点击了拒绝授权，将无法进入小程序，请授权之后再进入!!!',
                  showCancel: false,
                  confirmText: '返回授权',
                  success: function(res) {
                    
                    if (res.confirm) {
                      console.log('用户点击了“返回授权”'); 
                    }
                  }
       });
      }
})
}})