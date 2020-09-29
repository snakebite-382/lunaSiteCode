$(function(){
	// for every nav-link
	$('a.nav-link').each(function(){
		// if the link points to the current page
		if ($(this).prop('href') == window.location.href) {
			// add the active class for css
			$(this).addClass('active-page');

		}
	});
});