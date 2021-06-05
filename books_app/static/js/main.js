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
});