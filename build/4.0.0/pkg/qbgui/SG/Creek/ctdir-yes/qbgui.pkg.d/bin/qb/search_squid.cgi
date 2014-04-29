#!/usr/bin/perl
require ("/usr/local/apache/qb/language/qblanguage.cgi");
@qblang = QBlanguage();
BEGIN { unshift (@INC,"/usr/local/apache/qb/perl_lib"); }

use CGI;
my $form = new CGI;
my $title = $form->param('title');
my $mytitle;
if($title eq 'webfilter'){$mytitle = @qblang[636];}
#if($title eq 'webfilter'){$mytitle = 'Web Filter';}
if($title eq 'webcache'){$mytitle = @qblang[637];}
print "Content-type:text/html\n\n";
#---------------- Just for form to show available items of subnets and services ------------------
print qq (<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"> );
print qq (<!DOCTYPE html><html><head><meta charset="UTF-8">);
print qq (<link rel="stylesheet" href="jquery-ui-1.10.3.custom.css" />);
print qq (<script src="jquery-1.10.2.js"></script>);
print qq (<script type="text/javascript" src="../grid.js"></script>);
#print qq (<link rel="stylesheet" href="/resources/demos/style.css" />);
print qq (<script type="text/javascript" src ="sorttable.js"></script><script type="text/javascript" src ="../qbjs/jquery.js"></script><style type="text/css">#tables_filter{text-align: left;} td{slign:center;} table.sortable thead{background-color:#eee;color:#666666;font-weight: bold;cursor: default;}button.menu{margin-right: 4px;height:18px;font:10px Verdana;color:white;background:#336699;border:1px solid black;cursor:hand;}</style><link rel="stylesheet" href="../gui.css" type="text/css"></head><body bgcolor="#336699" text="#ffffff" link="#000040" >);
print qq (<div align="center" style="width: 100%; margin: 12px auto 5px auto;">);

print qq (<input id="title" value="$title" type="hidden">);
#------- start to draw every form object to interact with users --------------------------------
print qq(<form name="lantgaffic" method="post" action="lantraffic.cgi" style="width:100%">);
print qq (<table cellspacing="0" border="0">);
print qq (<tr><td class="bigtitle">$mytitle</td></tr></table>);
print qq (<div style="width:75%" >);
print qq (<table width="100%" border="1" ><tr>);
print qq (<td class="body" align="center">$qblang[771]</td>);
print qq (<tr><td class="body" align="center" >$qblang[772] : );
my ($sec, $min, $hour, $day, $mon, $year) = localtime(time);
if ($day < 10 ){$day='0'.$day;}
$mon++;
if ($mon < 10 ){$mon='0'.$mon;}
$now_date=join("/",($year+1900,$mon,$day));
print qq (<input type="text" id="datepicker" style="width:90px" value="$now_date"/>);
print qq (&nbsp<select id="start_hr">);
foreach my $tm (0..23 )
{
    if ($tm < 10 ){$tm = '0'.$tm;}
    print qq(<option value="$tm" >$tm</option>);
}
print qq (</select>);
print qq (<select id="start_sec" style="true">);
foreach my $tm (0..59 )
{
    if ($tm < 10 ){$tm = '0'.$tm;}
    print qq(<option value="$tm" >$tm</option>);
}
print qq (</select>);#$text);
print qq (<a name="noquery" >$qblang[775] : </a><select id="report_type" name="noquery">);
print qq (<option value="1">Daily</option>);
print qq (<option value="6">Per 5 minute</option>);
print qq (</select>&nbsp;&nbsp;);
print qq (&nbsp&nbsp&nbsp $qblang[774] : <input id="ip_search" value="">);
print qq (</td></tr>);

print qq (<tr><td align="center"><input type="button" id="query" value="$qblang[712]" onclick="Submit();">);
print qq (<input type="button" id="output" value="$qblang[713]" onclick="dataCSV();">);
print qq (</td></tr>);

print qq (</table></div>);

print qq (<img id="load_gif" src="image/loading.gif" style="display:none;">);

print << "QB_TRAFFIC";

<script src="jquery-ui-1.10.3.custom.js"></script>
<script src="jquery.ui.datepicker-zh-TW.js"></script>
<script src="../qbjs/jquery.dataTables.min.js"></script>
<script src="search.js"></script>
<script language="javascript">

\$( "#datepicker" ).datepicker({
    regional:"en-AU",
    defaultDate: "+1w",
	changeYear: true,
    changeMonth: true,
    numberOfMonths: 1,
    showButtonPanel: true,
    onClose: function( selectedDate ) {
        \$( "#datepicker_1" ).datepicker( "option", "minDate", selectedDate );
    }
});


function Submit()
{
	\$("#load_gif").css('display','block'); 
	\$("#query").attr('disabled', true);
     var url = "search_data_squid.pl";
	 var title = \$("#title").val();
     var start = \$("#datepicker").val();
     if (!start)
     {
         alert("ERROR");
         return;
     }
     var ip = \$("#ip_search").val();
     var domain = 'y';
     \$.get(url,{title:title,ip:ip,symd:start,domain:domain},function fno(data){
	\$("#table").html(data);
	var oTable =  \$('#tables').dataTable({
	    "bPaginate": false,
	    "bInfo": false
	});
	\$("label").attr("style","display:none");
        \$("#ip_search").keyup(function()
	{
    	    oTable.fnFilter(\$("#ip_search").val());
	});
	\$("#load_gif").css('display','none');
	\$("#query").attr('disabled', false);
     });
}

function search_squid(search_domain,title,ip,symd)
{
        \$("#load_gif").css('display','block');
        \$("#query").attr('disabled', true);
        var url = "search_data_squid.pl";
        var title = title;
        var ip = ip;
        var symd = symd;
        var search_domain = search_domain;
        \$.get(url,{search_domain:search_domain,title:title,ip:ip,symd:symd},function fno(data){
        \$("#table").html(data);
        var oTable =  \$('#tables').dataTable({
            "bPaginate": false,
            "bInfo": false
        });
        \$("label").attr("style","display:none");
        \$("#ip_search").keyup(function()
        {
            oTable.fnFilter(\$("#ip_search").val());
        });
        \$("#load_gif").css('display','none');
        \$("#query").attr('disabled', false);
     });
}

function search_squid_detail(title,ip,symd,request)
{
	\$("#load_gif").css('display','block'); 
	\$("#query").attr('disabled', true);
	var title = title;
	var ip = ip;
	var symd = symd;
	var request = request;
    var url = "search_data_squid_detail.pl";
    \$.get(url,{title:title,ip:ip,symd:symd,request:request},function fno(data){
	\$("#table").html(data);
	var oTable =  \$('#tables').dataTable({
	    "bPaginate": false,
	    "bInfo": false
	});
	\$("label").attr("style","display:none");
        \$("#ip_search").keyup(function()
	{
    	    oTable.fnFilter(\$("#ip_search").val());
	});
	\$("#load_gif").css('display','none');
	\$("#query").attr('disabled', false);
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
			trim = tr[i].cells[d].innerHTML.replace(/(^[\\s]*)|([\s]*\$)/g, "");
			}
			result = result+trim+',';
		}
		total_result = total_result + result.replace(/,\$/, '_');
    }
	//alert(total_result);
	window.open('flow_export.cgi?action=SAVE&total_result='+total_result,'Save as CSV');
}

</script>

QB_TRAFFIC

print qq (<div class="divframe" style="width:75%" id="table">);
print qq (</div></table>);
print qq(</form></div></body></html>);
