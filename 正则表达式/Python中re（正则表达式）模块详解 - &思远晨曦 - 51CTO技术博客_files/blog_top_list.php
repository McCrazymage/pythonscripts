
var start = 1;

var _html = '<div class="blogpopMain"><div class="l">'
          + '<a href="http://blog.51cto.com/zt/632" target="_blank"><img src="http://s3.51cto.com/wyfs02/M01/26/1F/wKiom1Np5wrDxLB-AAA1pdFfLtU174.jpg" width="105" height="105" /></a>'
          + '<p><a href="http://blog.51cto.com/zt/632" target="_blank">����DB2�ı�����ָ�</a></p></div>'
          + '<div class="r"><h4 style="text-align:left;"><a href="http://shenyisyn.blog.51cto.com/4968488/1406212" target="_blank">��ҵ��ҵCEO���ö��ٹ��ʣ�</a></h4>'
          + '<ul>'
          + '<li><a href="http://zhaisj.blog.51cto.com/219066/1406725" target="_blank">����Ϊ�û�д���б��顱��</a></li>'
          + '<li><a href="http://edu.51cto.com/course/course_id-1264.html" target="_blank"style="color:red;">5&#8226;12��:ר�ҷ�������̹��Դ���</a></li>'
          + '<li><a href="http://edu.51cto.com/course/course_id-1222.html" target="_blank">�����-��Ϣϵͳ����ʦ��Ƶ�̳�</a></li>'
          + '<li><a href="http://edu.51cto.com/course/course_id-1192.html" target="_blank"style="color:red;">�����Σ�Hive Pig Mahout�����ھ�</a></li>'
          + '</ul>'
          + '</div></div>'
          + '';

jQuery('#showMessagerDim').show();

jQuery(function(){
//window.onload=function(){
   if(get_cookie('blog_top')==''&&start==1){
//	 show_pop();
	    jQuery.messager.showblogtop('', _html);
        var date=new Date();
	    var day = 1399564800000;//
	    date.setTime(day);
	    var test = date.getTime();
	    document.cookie="blog_top=yes;domain=.blog.51cto.com;expires="+date.toGMTString()+";path=/;";
    }
	jQuery("#showMessagerDim").click(function(){
		jQuery.messager.showblogtop('', _html);
		//removeIframe();
	});
//}
});


function get_cookie(Name) {
    var search = Name + "=";
    var returnvalue = "";
    if (document.cookie.length > 0) {
        offset = document.cookie.indexOf(search);
        if (offset != -1) {
            offset += search.length;

            end1 = document.cookie.indexOf(";", offset);

            if (end1 == -1)
            end1 = document.cookie.length;
            returnvalue=unescape(document.cookie.substring(offset, end1));
        }
    }
    return returnvalue;
}

