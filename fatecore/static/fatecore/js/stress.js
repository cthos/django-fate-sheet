(function ($) {
  $(function () {
    $('.stress-box').click(function () {
      $(this).toggleClass('checked');
    });

    $('.reset-stress-button').on('click', 'a', function() {
      $('.stress-box.checked').removeClass('checked');
    });
  });
}) ($);
