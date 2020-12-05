$star_rating = $('.star-rating .fa')

SetRatingStar = ->
  $star_rating.each ->
    if parseInt($star_rating.siblings('input.rating-value').val()) >= parseInt($(this).data('rating'))
      $(this).removeClass('fa-star-o').addClass('fa-star')
    else
      $(this).removeClass('fa-star').addClass('fa-star-o')

$star_rating.on 'click', ->
    $star_rating.siblings('input.rating-value').val $(this).data('rating')
    SetRatingStar()

SetRatingStar()