document.querySelectorAll('.card__wishlist').forEach(button => {
    button.addEventListener('click', function() {
      this.classList.toggle('filled');
      if (this.classList.contains('filled')) {
        this.textContent = '♥ Wishlisted';
      } else {
        this.textContent = '♡ Wishlist';
      }
    });
  });