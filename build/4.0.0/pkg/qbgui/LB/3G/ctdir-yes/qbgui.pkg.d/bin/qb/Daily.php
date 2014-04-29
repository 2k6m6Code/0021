<!DOCTYPE html><html><head><meta charset="UTF-8">
<link rel="stylesheet" href="jquery-ui-1.10.3.custom.css" />
<link rel="stylesheet" href="../gui.css" type="text/css">
<script type="text/javascript" src="jquery-1.10.2.js"></script>
<script src="highcharts.min.js"></script>
<script src="exporting.js"></script>
<style>
.no-close .ui-dialog-titlebar-close {
    display: none;
    }
.ui-dialog-titlebar {
  font-size: 100% !important;
  background-color: #336699;
    background-image: none;
      color: #FFFF;
      }
.ui-dialog {
  font-size: 80% !important;
  background-color: #556677;
}
.ui-dialog-buttonpane {
  background-color: #556677;
  color: #FFFF;
}
.ui-dialog-content{
color:#0000;
} 
.ui-widget-content {
color:#0000;
}
</style>

</head>
<body bgcolor="#336699" text="#ffffff" link="#000040" >
<div align="center" style="width: 100%; margin: 12px auto 5px auto;">
<form name="lantgaffic" method="post" action="query.php" style="width:100%">
<table cellspacing="0" border="0">
<tr><td class="bigtitle" align="center">Daily Graphic_org</td></tr></table>
<div style="width:75%" align="center">
<table width="100%" border="1"><tr>
<td class="body" id="querycondition" align="center">Query Condition</td>
<tr><td class="body" align="center"><span id="datetime">Date Time</span> :
<?php
date_default_timezone_set("Asia/Taipei");
$now_TW=time();
$date_T_m_d = date('Y/m/d',$now_TW);
$date_h = date('H',$now_TW);
$date_i = date('i',$now_TW);
$date_s = date('s',$now_TW);
echo '<input type="text" id="datepicker" style="width:90px" value='.$date_T_m_d.">";


/* echo '<select id="start_hr">';
$date_h--;
for($x=0;$x<24;$x++)
{
    if ($x < 10)$x='0'.$x;
    if ($x == $date_h)
    	echo '<option value='.$x.' selected>'.$x.'</option>';
    else
    	echo '<option value='.$x.'>'.$x.'</option>';
}
echo '</select><a>Hour</a>';

echo '&nbsp;&nbsp;&nbsp;<a>IP : </a>';
echo '<input type="text" style="width:90px" value="" >&nbsp;&nbsp;&nbsp;'; */

?>

<tr><td align="center"><input type="button" id="query" value="Query" onclick="Submit();"></td></tr>
<!--
<tr><td align="center">
<input type="button" id="day" value="<<Day" onclick="Submit();">&nbsp;&nbsp;
<input type="button" id="hour" value="<<Hour" onclick="Submit();">&nbsp;&nbsp;
<input type="button" id="today" value="Today" onclick="Submit();">&nbsp;&nbsp;
<input type="button" id="Hour" value="Hour>>" onclick="Submit();">&nbsp;&nbsp;
<input type="button" id="Day" value="Day>>" onclick="Submit();">&nbsp;&nbsp;
</td></tr>
-->
</table></div>
<img id="load_gif" src="image/loading.gif" style="display:none;">
<div id="dialog" title="Result">
</div>
<div id="flows" style="width:75%;height:200px"></div>
<div id="bytes" style="width:75%;height:200px"></div>
<div id="packets" style="width:75%;height:200px"></div>
<div id="bps" style="width:75%;height:200px"></div>
<div id="pps" style="width:75%;height:200px"></div>
<div id="bpp" style="width:75%;height:200px"></div>
<script src="jquery-ui-1.10.3.custom.js"></script>
<script src="jquery.ui.datepicker-zh-TW.js"></script>
<script src="../qbjs/jquery.dataTables.min.js"></script>
<script language="javascript">
Submit();

var click_type='';

$( "#datepicker" ).datepicker({
    regional:"zh-TW",
    defaultDate: "+1w",
	changeYear: true,
    changeMonth: true,
    numberOfMonths: 1,
    showButtonPanel: true
});


function getcookie(name)
{
    var c=document.cookie.split("; ");
    for (var i=0; i<c.length; i++)
    {
       var b=c[i].split("=");
       if(name==b[0]) { return unescape(b[1]); }
    }
                          
    return;
}

if ( getcookie('locale') == "zh_TW" )
{
    $("td[class='bigtitle']").html("每日圖表");
    $("#querycondition").html("查詢條件");
    $("#query").val("查詢");
    $("#datetime").html("時間");
}
else
    $("td[class='bigtitle']").html("Daily Graphic");

function Submit()
{
	$("#load_gif").css('display','block'); 
	$("#query").attr('disabled', true);
    var time = document.getElementById("datepicker").value;
    var tmp = new Array();
    tmp = time.split("/");
    var option=tmp[0]+tmp[1]+tmp[2];
	var y=tmp[0];
	var m=tmp[1];
	var d=tmp[2];
$.ajax({
    url: 'image_data.php',
    cache: false,
    dataType: 'html',
    type:'GET',
    data: { option:option},
    error: function(xhr) {
        alert('Ajax request ERROR');
    },
    success: function(response) {
        var test = new Array();
        test = response.split(",:");
        for (var i=0;i<test.length;i++)
        {
            var tmp = new Array();
            tmp = test[i].split(/-:/);
            if (tmp[0].match("flows") == "flows")
            {
               var tmp_1 = new Array();
               var tmp_2 = new Array();
               tmp_1 = tmp[1].split(/,/);
               for(var x=0;x<tmp_1.length;x++)
               {
                   tmp_2[x]=(tmp_1[x]++);
               } 
               creat_map('flows',tmp_2,y,m,d);
            }
            if (tmp[0].match("bytes") == "bytes")
            {
               var tmp_1 = new Array();
               var tmp_2 = new Array();
			   var num = tmp[1].replace(/\w\,/g,',');
			   num = num.replace(/\w$/g,'');
			   //alert(num);
			   tmp_1 = num.split(/,/);
               //tmp_1 = tmp[1].split(/,/);
               for(var x=0;x<tmp_1.length;x++)
               {
                   tmp_2[x]=(tmp_1[x]++);
               } 
               creat_map('bytes',tmp_2,y,m,d);
            }
            if (tmp[0].match("packets") == "packets")
            {
               var tmp_1 = new Array();
               var tmp_2 = new Array();
               tmp_1 = tmp[1].split(/,/);
               for(var x=0;x<tmp_1.length;x++)
               {
                   tmp_2[x]=(tmp_1[x]++);
               } 
               creat_map('packets',tmp_2,y,m,d);
            }
            if (tmp[0].match("bps") == "bps")
            {
               var tmp_1 = new Array();
               var tmp_2 = new Array();
               tmp_1 = tmp[1].split(/,/);
               for(var x=0;x<tmp_1.length;x++)
               {
                   tmp_2[x]=(tmp_1[x]++);
               } 
               creat_map('bps',tmp_2,y,m,d);
            }
            if (tmp[0].match("pps") == "pps")
            {
               var tmp_1 = new Array();
               var tmp_2 = new Array();
               tmp_1 = tmp[1].split(/,/);
               for(var x=0;x<tmp_1.length;x++)
               {
                   tmp_2[x]=(tmp_1[x]++);
               } 
               creat_map('pps',tmp_2,y,m,d);
            }
            if (tmp[0].match("bpp") == "bpp")
            {
               var tmp_1 = new Array();
               var tmp_2 = new Array();
               tmp_1 = tmp[1].split(/,/);
               for(var x=0;x<tmp_1.length;x++)
               {
                   tmp_2[x]=(tmp_1[x]++);
               } 
               creat_map('bpp',tmp_2,y,m,d);
            }
            
        }
		$("#load_gif").css('display','none');
		$("#query").attr('disabled', false);
    }
});
}

Highcharts.setOptions({
global: {
useUTC: ture
}
});

function creat_map(o,a,y,m,d)
{
	var Today=new Date();
	var y=y;
	var m=m-1;
	var d=d
    $('#'+o).highcharts({
    	title:{
            text:o
    	},
    	xAxis:{
	    type:'datetime',
	    maxZoom:24*3600000,//fourteendays
    	    title:{
	    	text:null
    	    }
        },
	yAxis:{
	    title:{
		text:''
	    }
	},
	tooltip:{
	    shared:true
	},
	legend:{
	    enabled:false
	},
	plotOptions:{
	    area:{
		fillColor:{
		    linearGradient:{x1:0,y1:0,x2:0,y2:1},
		    stops:[
			[0,Highcharts.getOptions().colors[0]],
			[1,Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
		    ]
		},
		lineWidth:1,
		marker:{
		    enabled:false
		},
		shadow:false,
		    states:{
		    	hover:{
			    lineWidth:1
			}
		    },
		    threshold:null
		    }
		},
		series:[{
		    type:'area',
		    name:o,
		    pointInterval:1800000,
		    pointStart:Date.UTC(y,m,d),
		    data:a,
		    point:{
		    	events:{
		        	click: function(event) {
		        	$("#dialog").css("color","white");
		        	var datetime = unix_to_datetime((this.x/1000)-(8*60*60));
		        	var tmp = datetime.split("-");
		        	var endh = parseInt(tmp[3]);
		        	var endm = '00';
		        	click_type=o;
		        	if(tmp[4] == '00'){endm = '30';}else{endh= endh+1;}
		        	if(endh < 10){endh = '0'+endh;}
		        	var time = 'nfcapd.'+tmp[0]+tmp[1]+tmp[2]+tmp[3]+tmp[4]+':nfcapd.'+tmp[0]+tmp[1]+tmp[2]+endh+endm;
		        	var limit = '-s record/'+o;
		        	var symd = tmp[0]+"/"+tmp[1]+"/"+tmp[2];
		        	var option = 'realtime';
		        	var group = 'view_group';
		        	var url = "search_data.pl";
				$.get(url,{time:time,limit:limit,symd:symd,option:option,group:group},function fno(data){
		        		$("#dialog").html(data);
		        		var oTable =  $('#tables').dataTable({
		        			"timeout": 5000,
		        			"bPaginate": false,
		        			"bInfo": false
		        		});
		        	        $("label").attr("style","display:none");
		        	        //\$("#ip_search").keyup(function()
		        	        //{
		        	        //	oTable.fnFilter(\$("#ip_search").val());
		        	        //});
                                        //\$("#load_gif").css('display','none');
  	                        });
//		        	$('#dialog').html( (this.x/1000)-(8*60*60)+"<br>"+time+"<br>"+limit);
//		        	$('#dialog').html( this.x+' '+this.y );
		        	$( "#dialog" ).dialog({
		        		width: 800,
		        		height: 560,
		        		closeText: 'Close me',
		        		dialogClass: "no-close",
					buttons: [{
		        			text: "Close",
		        		        click: function() {
		        		        	$( this ).dialog( "close" );
		        		        }
		        		}]
		        	});
		        	}
                    	}
                    }
		}]
	});

}

function datetime_to_unix(datetime){
	var arr = datetime.split("-");
	var now = new Date(Date.UTC(arr[0],arr[1],arr[2],'00','00','00'));
	return parseInt(now.getTime()-8*60*60);
}

function unix_to_datetime(unix) {
	var now = new Date(parseInt(unix)*1000);
	var M = now.getMonth()+1;
	var D = now.getDate();
	var H = now.getHours();
	var MM = now.getMinutes();
	if(M < 10){M='0'+M};
	if(D < 10){D='0'+D};
	if(H < 10){H='0'+H};
	if(MM < 10){MM='0'+MM};
	var result = now.getFullYear()+"-"+M+"-"+D+"-"+H+"-"+MM;
	return result.toString();
}

function search_flow(ip,time,option,symd,proto)
{
	//$("#load_gif").css('display','block');
        var ip = ip;
        var time = time;
        var option = option;
        var symd = symd;
        var proto = proto;
        var url = "search_flow.pl";
        $.get(url,{ip:ip,time:time,option:option,symd:symd,proto:proto},function fno(data){
        	$("#dialog").html(data);
                var oTable =  $('#tables').dataTable({
                	"timeout": 5000,
                        "bPaginate": false,
                        "bInfo": false
                });
                $("label").attr("style","display:none");
        //        $("#ip_search").keyup(function()
        //        {
        //        	oTable.fnFilter(\$("#ip_search").val());
        //        });
        //        $("#load_gif").css('display','none');
        });
}

function search_group(ip,time,option,symd,proto)
{
	//$("#load_gif").css('display','block');
        var ip = ip;
        var time = time;
        var limit = '-s record/'+click_type;
        var option = option;
        var symd = symd;
        var proto = proto;
        var url = "search_data.pl";
        $.get(url,{ip:ip,time:time,limit:limit,option:option,symd:symd,unit:proto},function fno(data){
        	$("#dialog").html(data);
        	var oTable =  $('#tables').dataTable({
        		"timeout": 5000,
                	"bPaginate": false,
                	"bInfo": false
        	});
        $("label").attr("style","display:none");
        });
}


</script>
</body></html>
