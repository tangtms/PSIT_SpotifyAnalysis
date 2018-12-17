
var Gallery = (function() {
    var colors = ['#34495E', '#2E4053', '#283747', '#212F3C', '#1B2631', '#2C3E50', '#273746'];
    var scrollTimeId;
    var posLeft = 0;

    function Gallery(config) {
        this.list = $(config.list);
        this.items = this.list.find('li');
        this.itemWidth = this.items.outerWidth();
    };

    Gallery.prototype = {
        constructor: Gallery,

        init: function() {
            this.setGalleryWidth();
            this.setItemsColor();
            this.eventManager();

            return this;
        },

        eventManager: function() {
            var _this = this;

            $("html, body").on('mousewheel', function(event) {
                clearTimeout(scrollTimeId);
                scrollTimeId = setTimeout(onScrollEventHandler.bind(this, event, _this.itemWidth), 0);
            });
        },

        getRandomColor: function() {
            return colors[Math.floor(Math.random() * colors.length)];
        },

        setItemsColor: function() {
            var _this = this;

            $.each(this.items, function(index, item) {
                 item.style.backgroundColor = _this.getRandomColor();
            });
        },

        setGalleryWidth: function() {
            this.list.css('width', this.getGalleryWidth());
        },

        getGalleryWidth: function() {
            var width = 0;

            this.items.each(function(index, item) {
                width += $(this).outerWidth();
            });

            return width;
        }
    };

    function onScrollEventHandler(event, width) {
      if (event.deltaY > 0) {
        this.scrollLeft -= width / 2;
      } else {
        this.scrollLeft += width / 2;
      }
 
        // Firefox, please, stop it
         // if (navigator.userAgent.toLowerCase().indexOf('firefox') > -1) {
         //    if (event.originalEvent.detail > 0) {
         //        posLeft += width / 2;
         //        $('html').scrollLeft(posLeft);
         //    } else {
         //        posLeft -= width / 2;
         //        $('html').scrollLeft(posLeft);
         //    }
         // } else {
         //    if (event.originalEvent.wheelDelta > 0)  {
         //        this.body.scrollLeft -= width / 2;
         //    } else {
         //        this.body.scrollLeft += width / 2;
         //    }
         // }
        event.preventDefault();
    };

    return Gallery;
})();


$(document).ready(function() {
    var gallery = new Gallery({
        list: '.gallery'
    }).init();
});