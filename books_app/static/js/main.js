$(document).ready(function () {
	console.log("HELLO")
	$('#sidebarCollapse').on('click', function () {
		$('#sidebar').toggleClass('active');
	});
	$('.column').hover(function(){
		$(this).children('img').addClass('hide');
		$(this).children('p').removeClass('hide');},
		function(){
		$(this).children('p').addClass('hide');
		$(this).children('img').removeClass('hide');});

	$(function(){
		$('.selling').on('click',function(e){
			$('.to_exchange').css('display','none');
			$('.pricing').css('display','inline');
			e.preventDefault();
		});
	});
	$(function(){
		$('.exchanged').on('click',function(e){
			$('.pricing').css('display','none');
			$('.to_exchange').css('display','inline');
			e.preventDefault();
		});
	});
	$(function(){
		$('.bothing').on('click',function(e){
			$('.pricing').css('display','inline');
			$('.to_exchange').css('display','inline');
			e.preventDefault();
		});
	});
	
});
