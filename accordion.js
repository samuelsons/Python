jQuery(function() {
const img = "";
  jQuery("#elementor-tab-title-").click(function(){
    jQuery(".toggle-img img").attr('srcset',img);
     jQuery(".toggle-img img").attr('src',img);
  });
});
