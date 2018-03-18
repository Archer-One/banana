Set objEmail = CreateObject("CDO.Message")  
Call SendMail()  
  
Sub SendMail  
<<<<<<< HEAD
        objEmail.From = "@qq.com" '发件人  
        objEmail.To = "@qq.com" '收件人  
=======
        objEmail.From = "***@qq.com" '发件人  
        objEmail.To = "***@qq.com" '收件人  
>>>>>>> 422ff702258a74dec92341f8f0244d0ed1888b85
        objEmail.Subject = "测试" '电子邮件主题主题  
        objEmail.Textbody = "测试内容请勿拒收" '电子邮件内容  
        objEmail.AddAttachment "C:\3.jpg"   
        objEmail.Configuration.Fields.Item _  
            ("http://schemas.microsoft.com/cdo/configuration/sendusing") = 2
        objEmail.Configuration.Fields.Item _  
            ("http://schemas.microsoft.com/cdo/configuration/smtpserver") = "smtp.qq.com" 'SMTP服务器地址  
        objEmail.Configuration.Fields.Item _  
<<<<<<< HEAD
            ("http://schemas.microsoft.com/cdo/configuration/sendusername") = "@qq.com" '用户名  
=======
            ("http://schemas.microsoft.com/cdo/configuration/sendusername") = "***@qq.com" '用户名  
>>>>>>> 422ff702258a74dec92341f8f0244d0ed1888b85
        objEmail.Configuration.Fields.Item _  
            ("http://schemas.microsoft.com/cdo/configuration/sendpassword") = "***" '密码  
        objEmail.Configuration.Fields.Item _  
            ("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate") =1'明文验证  
        objEmail.Configuration.Fields.Item _  
            ("http://schemas.microsoft.com/cdo/configuration/smtpserverport") = 465 'SMTP端口号  
        objEmail.Configuration.Fields.Item _  
            ("http://schemas.microsoft.com/cdo/configuration/smtpusessl") = True '使用SSL  
        objEmail.Configuration.Fields.Item _  
            ("http://schemas.microsoft.com/cdo/configuration/smtpconnectiontimeout") = 60 '超时  
        objEmail.Configuration.Fields.Update  
        objEmail.Send  
End Sub  
