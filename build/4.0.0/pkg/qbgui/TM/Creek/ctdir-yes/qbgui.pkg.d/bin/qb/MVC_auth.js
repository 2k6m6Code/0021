var myapp={};

myapp.Model = function(){

   this.init = function(){
       $( "#datepicker" ).datepicker({
           regional:"en-AU",
           defaultDate: "+1w",
           changeMonth: true,
           numberOfMonths: 1,
           showButtonPanel: true,
      });
      var dy = new Date(); 
      $( "#datepicker" ).val(dy.getFullYear()+"/"+(dy.getMonth()+1)+"/"+dy.getDate());
   };
   
   this.query = function(in_date,in_data){
   	$("#query").attr('disabled', true);
  	$.get('viewflow.pl',{type:'auth',date:in_date,dig:in_data},function(request){
  	    $("#table").html(request);
  	    var oTable =  $('#tables').dataTable({
  	        "bPaginate": false,
  	        "bInfo": false
  	    });
  	    $("label").attr("style","display:none");
  	    $("#ip_search").keyup(function(){
  	        oTable.fnFilter($("#ip_search").val());
  	    });
  	    $("#load_gif").css('display','none');
  	    $("#query").attr('disabled', false);
  	});
   };
   
   this.output = function()
	{
		alert('asdfasdf');
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
	};
};

myapp.Presenter = function(){
    var model = null;
    this.init = function(){
        model=new myapp.Model();
        model.init();
    };
    
    this.query = function(in_date,in_data){
        model.query(in_date,in_data);
    };
    
};

myapp.view={
    $button_add: null,
    $input_date: null,
    $input_search: null,
    presenter:null,
    init : function(){
   	this.presenter = new myapp.Presenter();
   	this.$button_add = $("#query");
   	this.$input_date = $("#datepicker");
   	this.$input_search = $("#ip_search");
   	this.presenter.init();
   	this.bindEvents();
    },
    bindEvents:function(){
        var view = this;
        var presenter = this.presenter;
        
        this.$button_add.click(function(){
            presenter.query(view.$input_date.val());
        });
    }
};





$(function(){
    myapp.view.init();
});

