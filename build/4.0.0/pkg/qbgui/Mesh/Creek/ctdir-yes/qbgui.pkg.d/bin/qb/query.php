<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<!DOCTYPE html><html><head><meta charset="UTF-8">
<link rel="stylesheet" href="jquery-ui-1.10.3.custom.css" />
<script src="jquery-1.9.1.js"></script>
<script type="text/javascript" src="../grid.js"></script>
<link rel="stylesheet" href="/resources/demos/style.css" />
<script type="text/javascript" src ="sorttable.js"></script>
<script type="text/javascript" src ="../qbjs/jquery.js"></script>
<style type="text/css">
#tables_filter{text-align: left;}table.sortable thead{background-color:#eee;color:#666666;font-weight: bold;cursor: default;}
button.menu{margin-right: 4px;height:18px;font:10px Verdana;color:white;background:#336699;border:1px solid black;cursor:hand;}</style>
<link rel="stylesheet" href="../gui.css" type="text/css"></head>
<body bgcolor="#336699" text="#ffffff" link="#000040" >
<div align="center" style="width: 100%; margin: 12px auto 5px auto;">
<input id="option" value="realtime" type="hidden">
<form name="lantgaffic" method="post" action="query.php" style="width:100%">
<table cellspacing="0" border="0">
<tr><td class="bigtitle" align="center"></td></tr></table>
<div style="width:75%" align="center">
<table width="100%" border="1"><tr>
<td class="body" id="querycondition" align="center">Query Condition</td>
<tr><td class="body" align="center"><span id="datetime">Date Time </span> : 
<?php
date_default_timezone_set("Asia/Taipei");
$now_TW=time();
$date_T_m_d = date('Y/m/d',$now_TW);
$date_h = date('H',$now_TW);
$date_i = date('i',$now_TW);
$date_s = date('s',$now_TW);
echo '<input type="text" id="datepicker" style="width:90px" value='.$date_T_m_d.">";
echo '<select id="start_hr">';
$date_h--;
for($x=0;$x<24;$x++)
{
    if ($x < 10)$x='0'.$x;
    if ($x == $date_h)
        echo '<option value='.$x.' selected>'.$x.'</option>';
    else
        echo '<option value='.$x.'>'.$x.'</option>';
}
echo '</select>';
echo '<select id="start_sec">';
for($x=0;$x<60;$x++)
{
    if ($x < 10)$x='0'.$x;
    if ($x == $date_i)
        echo '<option value='.$x.' selected>'.$x.'</option>';
    else
        echo '<option value='.$x.'>'.$x.'</option>';
}
echo '</select>-->';
echo '<input type="text" id="datepicker_1" style="width:90px;$display" value='.$date_T_m_d.'> ';
echo '<select id="end_hr">';
$date_h++;
for($x=0;$x<24;$x++)
{
    if ($x < 10)$x='0'.$x;
    if ($x == $date_h)
        echo '<option value='.$x.' selected>'.$x.'</option>';
    else
        echo '<option value='.$x.'>'.$x.'</option>';
}
echo '</select>';
echo '<select id="end_sec">';
for($x=0;$x<60;$x++)
{
    if ($x < 10)$x='0'.$x;
    if ($x == $date_i)
        echo '<option value='.$x.' selected>'.$x.'</option>';
    else
        echo '<option value='.$x.'>'.$x.'</option>';
}
echo '</select>';
//echo '&nbsp;&nbsp;Core Switch :';
//echo '<select id="core_switch"><option value="all">ALL</option></select>&nbsp;&nbsp;';
echo '</td></tr>';
?>
<tr><td class="body" align="center">
<span id="sourceip"> Source IP </span>:<input id="srcip" value="" size=15>
<span id="srcportkey"> Src Port </span>:<input id="srcport" value="" size=3>
<span id="destinationip"> Destination IP </span>:<input id="dstip" value="" size=15>
<span id="dstportkey"> Dst Port </span>:<input id="dstport" value="" size=3>
<span id="flowdirection"> Flow Direction </span>:<select id="flow_dst">

<option value="-A srcip,dstip">Any</option>
<option value="-A srcip,dstip">Inbound</option>
<option value="-A srcip,dstip">Outbound</option>
<option value="local">Local</option>
<option value="-B ">BiDirection</option>
</select>
</td></tr>
<tr><td class="body" align="center">
<span id="groupby">Group By</span> : <select id="flow_dst_1" >
<option value="">IP</option>
<option value=",srcport">Src Port</option>
<option value=",dstport">Dst Port</option>
</select>
<span id="ipprotocol">IP Protocol</span> :
<select id="" >
<option value="">ALL</option>
<option value="">IPv4</option>
<option value="">IPv6</option>
</select>
<span id="protocol">Protocol : </span>
<select id="proto" >
<option value="all">ALL</option>
<option value="ICMP">ICMP</option>
<option value="IGMP">IGMP</option>
<option value="TCP">TCP</option>
<option value="UDP">UDP</option>
</select>
<span id="orderby">Order by </span>
<select id="order" >
<option value="-s record/bytes ">Bytes</option>
<option value="-s record/flows ">Flows</option>
</select>
<span id="span-top">Top </span>
<select id="top_1" >
<option value="-n 10">10</option>
<option value="-n 20">20</option>
<option value="-n 50">50</option>
<option value="-n 100">100</option>
<option value="-n 200">200</option>
<option value="-n 500">500</option>
</select>
</td></tr>
<tr><td align="center"><input type="button" id="query" value="Query" onclick="Submit();">
<input type="button" id="output" value="Save as CSV" onclick="dataCSV();">
</td></tr>
</table></div>

<img id="load_gif" src="image/loading.gif" style="display:none;">

<script src="jquery-ui-1.10.3.custom.js"></script>
<script src="jquery.ui.datepicker-zh-TW.js"></script>
<script src="../qbjs/jquery.dataTables.min.js"></script>
<script src="search.js"></script>
<script language="javascript">

$( "#datepicker" ).datepicker({
    regional:"zh-TW",
    defaultDate: "+1w",
    changeMonth: true,
    numberOfMonths: 1,
    showButtonPanel: true,
    onClose: function( selectedDate ) {
        $( "#datepicker_1" ).datepicker( "option", "minDate", selectedDate );
    }
});
                                    
$( "#datepicker_1" ).datepicker({
    regional:"zh-TW",
    defaultDate: "+1w",
    changeMonth: true,
    numberOfMonths: 1,
    showButtonPanel: true,
    onClose: function( selectedDate ) {
        $( "#datepicker" ).datepicker( "option", "maxDate", selectedDate );
    }
});

function Submit()
{
	$("#load_gif").css('display','block'); 
	$("#query").attr('disabled', true);
     var url = "search_data.pl";
	 var option = $("#option").val();
     var start = $("#datepicker").val();
     var end = $("#datepicker_1").val();
     if (!start || !end)
     {
         alert("ERROR");
         return;
     }
     var tmp = new Array;
     tmp=start.split("/");
     var time = "nfcapd." + tmp[0] + tmp[1] + tmp[2] + $("#start_hr").val() + $("#start_sec").val() + ":";
     tmp=end.split("/");
     time += "nfcapd." + tmp[0] + tmp[1] + tmp[2] + $("#end_hr").val() + $("#end_sec").val();
     var top = $("#top_1").val();
     if ($("#flow_dst").val() == "-B")
         var ip = $("#flow_dst").val();
     else
         var ip = $("#flow_dst").val() + $("#flow_dst_1").val();
     var limit= $("#order").val(); 
     var proto = $("#proto").val();
     $.get(url,{time:time,ip:ip,limit:limit,top:top,option:option,symd:start,proto:proto},function fno(data){
         $("#table").html(data);
         var oTable =  $('#tables').dataTable({
             "bPaginate": false,
             "bInfo": false
         });
         $("label").attr("style","display:none");
         
         $("#srcip").keyup(function(){
             oTable.fnFilter( $("#srcip").val());
         });
         
         $("#srcport").keyup(function(){
             oTable.fnFilter( $("#srcport").val());
         });
         
         $("#dstip").keyup(function(){
             oTable.fnFilter( $("#dstip").val());
         });
         
         $("#dstport").keyup(function(){
             oTable.fnFilter( $("#dstport").val());
         });
		 $("#load_gif").css('display','none');
		$("#query").attr('disabled', false);
     });
}

function search_flow(ip,time,option,symd,tm_ip)
{
	$("#load_gif").css('display','block'); 
    var ip = ip;
    var time = time;
    var option = option;
	var tm_ip = tm_ip;
    var url = "search_flow.pl";
    $.get(url,{ip:ip,time:time,option:option,symd:symd,tm_ip:tm_ip},function fno(data){
        $("#table").html(data);
        var oTable =  $('#tables').dataTable({
			"bPaginate": false,
			"bInfo": false
        });
        $("label").attr("style","display:none");
        $("#ip_search").keyup(function()
        {
			oTable.fnFilter($("#ip_search").val());
        });
		$("#load_gif").css('display','none');
	});
}

function dataCSV()
{
	var total_result = '';
	var tr = document.getElementById('tables').rows;
	var tr_total = tr.length;
	for (var i = 0; i < tr_total; i++)
    {
		var result = '';
		var td_total = tr[i].cells.length;
        for (var d = 0; d < td_total; d++)
		{
			var trim = tr[i].cells[d].innerHTML;
			if(d>1)
			{
			trim = tr[i].cells[d].innerHTML.replace(/(^[\s]*)|([\s]*$)/g, "");
			}
			result = result+trim+',';
		}
		total_result = total_result + result.replace(/,$/, '_');
    }
	//alert(total_result);
	window.open('flow_export.cgi?action=SAVE&total_result='+total_result,'Save as CSV');
}
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
    $("td[class='bigtitle']").html("即時流量查詢");
    $("#querycondition").html("查詢條件"); 
    $("#query").val("查詢") ;
    $("#output").val("儲存成CSV") ;
    $("#datetime").html("時間");
    
    $("#sourceip").html("來源位址");
    $("#srcportkey").html("來源端口");
    $("#destinationip").html("目的地位址");
    
    $("#dstportkey").html("目的地端口");
    $("#flowdirection").html("流量方向") ;
   
    $("#groupby").html("群組依");
    
    $("#ipprotocol").html("IP協定");
    $("#protocol").html("網路協定");

    $("#orderby").html("依照順序");
    $("#span-top").html("流量統計前");
//    $("#").html();
    
    //alert ( $("#groupby").html() );
    
}
else
    $("td[class='bigtitle']").html("Realtime Query");

</script>

<div class="divframe" style="width:75%" id="table">
</div></table>
</form></div></body></html>
