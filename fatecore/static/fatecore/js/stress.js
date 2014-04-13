(function ($) {
  $(function () {
    $('.checkable').click(function () {
      $(this).toggleClass('checked');
    });

    $('.reset-stress-button').on('click', 'a', function() {
      $('.stress-box.checked').removeClass('checked');
    });

    $('.consequences .checkable').click(function () {
      var tar = $(this).data('target');

      $('.' + tar).toggle('fast');
    });
  });
}) ($);
