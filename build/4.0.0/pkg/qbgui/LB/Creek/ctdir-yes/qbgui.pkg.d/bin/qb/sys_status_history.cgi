#!/usr/bin/perl
use Data::Dumper;
use CGI;
require ("qbmod.cgi");



print "Content-type:text/html\n\n";

#---------------- Just for form to show available items of subnets and services ------------------
my  %action;
my  $form = new CGI;

print qq (<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">);
print qq (<link rel="stylesheet" href="gui.css" type="text/css"/>);
print qq (<script type="text/javascript" src="jquery-1.10.2.js"></script>);
print qq (<script type="text/javascript" src="jquery-ui-1.10.3.custom.js"></script>);
print qq (<script type="text/javascript" src="qbjs/jquery.dataTables.min.js"></script>);
print qq (<script type="text/javascript" src="jquery.sparkline.js"></script>);
print qq (<script type="text/javascript" src="qbjs/sorttable.js"></script>);

print qq (<script src="jquery.ui.datepicker-zh-TW.js"></script>);
print qq (<script src="highcharts.min.js"></script>);
print qq (<script src="exporting.js"></script>);
print qq (<script type="text/javascript" src="highslide-full.js"></script>);
print qq (<script type="text/javascript" src="highslide.config.js" charset="utf-8"></script>);
print qq (<link rel="stylesheet" type="text/css" href="http://www.highcharts.com/highslide/highslide.css" />);
print qq (</head>);
print qq (<body bgcolor="#336699" text="#ffffff" link="#000040" >);


print qq(<div align="center">);
#------- start to draw every form object to interact with users --------------------------------
print qq(<form name="scheduleform" method="post" action="">);
print qq (<table cellspacing="0" border="0">);
print qq (<tr><td>);

#===========================================
print qq (<table bgcolor="#336699" cellspacing="3" border="0">);
    print qq (<tr><td class="">);

    #==============================================================
    # Print Title first
    # show
    #===============================================================	
	print qq (<div id="cpu" style="min-width: 800px; height: 50px; margin: 0 auto"></div>);
	print qq (<br>);
	print qq (<div id="mem" style="min-width: 800px; height: 50px; margin: 0 auto"></div>);
	print qq (<br>);
	print qq (<div id="cache" style="min-width: 800px; height: 50px; margin: 0 auto"></div>);
	print qq (<br>);
	print qq (<div id="ram" style="min-width: 800px; height: 50px; margin: 0 auto"></div>);
	print qq (<br>);
	print qq (<div id="session" style="min-width: 800px; height: 50px; margin: 0 auto"></div>);

#===========================================

print qq(</form></div>);
print qq(</body></html>);

print << "QB";
<script language="javascript">

function Submit()
{
	var status = new Array('cpu','mem','ram','cache','session');
	for(var i=0;i<status.length;i++)
	{
		get_picture(status[i]);
		//\$("#"+status[i]).parent("td").prev("td").attr("style","width:30%;align:left;");
	}
}			
			
			
function get_picture(status)
{
	\$.ajax({
	    url:'system_usage.pl',
    	    cache:false,
    	    dataType: 'html',
    	    type:'GET',
    	    data: {id:status},
    	    error: function(xhr){
    	    },
    	    success: function(response) {
		var dd = new Array();
		var yy = new Array();
    	        var data=new Array();
    	        yy=response.split(/--/);
    	        dd=yy[1].split(/ %/);
    	        
    	        for(var x=0;x<dd.length;x++)
		    if(dd[x]!='')
		    {
			data[x]=(dd[x]++);
		    }
        	//creat_picture(data,status);

			
		creat_map(status,data,yy[0]);
    	    }
        });
}

function creat_picture(data,name)
{
    \$("#"+name).sparkline(data, {
        type: 'line',width: '100%',height: '40',lineWidth: 1.5,spotRadius: 2});
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

function creat_map(name,data,yy)
{
	var Today=new Date();
	var xx=new Array();
	xx=yy.split(/:/);
	var title,content,unit='';
	if ( getcookie('locale') == "zh_TW" )
	{
		 if(name == 'cpu'){title='CPU使用率'; content='CPU Usage'; unit='%';}
	    else if(name == 'mem'){title='記憶體使用率'; content='Memory Usage'; unit='M';}
	    else if(name == 'cache'){title='快取記憶體使用率'; content='Cache Usage'; unit='M';}
	    else if(name == 'ram'){title='Ramdisk使用率'; content='Ramdisk Usage'; unit='M';}
	    else if(name == 'session'){title='現行連線數目'; content='Active Sessions'; unit='Quantity';}
	}
	else
	{
		 if(name == 'cpu'){title='CPU Usage'; content='CPU Usage'; unit='%';}
	    else if(name == 'mem'){title='Memory Usage'; content='Memory Usage'; unit='M';}
	    else if(name == 'cache'){title='Cache Usage'; content='Cache Usage'; unit='M';}
	    else if(name == 'ram'){title='Ramdisk Usage'; content='Ramdisk Usage'; unit='M';}
	    else if(name == 'session'){title='Active Sessions'; content='Active Sessions'; unit='Quantity';}
	}
        \$("#"+name).highcharts({
            chart: {
                zoomType: 'x',
                spacingRight: 20
            },
            title: {
                text: title
            },
            subtitle: {
                text: document.ontouchstart === undefined ?
                    'Click and drag in the plot area to zoom in' :
                    'Pinch the chart to zoom in'
            },
            xAxis: {
                type: 'datetime',
                maxZoom: 60*1000, // fourteen days
                title: {
                    text: null
                }
            },
            yAxis: {
                title: {
                    text: unit
                }
            },
            tooltip: {
                shared: true
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                area: {
                    fillColor: {
                        linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1},
                        stops: [
                            [0, Highcharts.getOptions().colors[0]],
                            [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                        ]
                    },
                    lineWidth: 1,
                    marker: {
                        enabled: false
                    },
                    shadow: false,
                    states: {
                        hover: {
                            lineWidth: 1
                        }
                    },
                    threshold: null
                }
            },
    
            series: [{
                type: 'area',
                name: content,
                pointInterval: 60*1000,
		pointStart:Date.UTC(Today.getFullYear(),Today.getMonth(),Today.getDate(),xx[0],xx[1]),
                data:data
            }]
        });
}
    


Submit();
</script>
QB
