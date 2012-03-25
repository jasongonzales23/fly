/* Author: Jason Gonzales
*/

$(document).ready(function(){

var n = 0 ;
var len = $('.slide').length - 1;

        
	function runIt(){
		if ( n > len ) { n = 0 };
		
		//hide stuff
		$('.slide').hide();
		$('.slideText').hide();
		$('.slide-thumb').removeClass('active');
        
        //show the image
		$('.slide').eq(n).fadeIn(500);
        $('.slideText').eq(n).fadeIn(500);	
		$('.slide-thumb').eq(n).addClass('active')/*.hide().fadeIn(500)*/;
		
		n++;
	}
	
	runIt();
	var t=setInterval(runIt,7000);
	
	//remove and replace with a hover command
    $('.slide-thumb').hover(function(e){
		n = $(this).index('.slide-thumb');
        console.log(n);
		clearInterval(t);
		$('.slide-thumb').stop(false, true);
        $('.slideText').stop(false, true);
		runIt();
		return false;
	},
	function(){t=setInterval(runIt,7000);}
	);
    
    //for touch devices?
    $('.slide-thumb').click(function(e){
		n = $(this).index('.slide-thumb');
		clearInterval(t);
		runIt();
		return false;
	});    

    $('#subnav h2').click(
        function(){
            //show the right stuff in presentation area
            $thisClass = $(this).attr('class');
            $('#presentation').children().hide();
            $('#presentation').children('.'+$thisClass).show();
            
            //change class of subnav
            $('#subnav').find('a').removeClass('selected');
            $(this).find('a').addClass('selected');
            return false;
        }
    );

    $('#contactForm').validate({
        rules: {
          email: {
            required: true,
            email: true
          }
        }
    });
    
});


























