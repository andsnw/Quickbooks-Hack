Template.mainLayout.onRendered(() => {
  var hasLoaded = Session.get('hasLoaded');
  if (hasLoaded !== true) {
    var scriptsToLoad = `
    <script type="text/javascript" src="/assets/js/jquery.min.js"></script>
    <script type="text/javascript" src="/assets/js/popper.min.js"></script>
    <script type="text/javascript" src="/assets/js/jquery.smartWizard.min.js"></script>
    <script type="text/javascript" src="/assets/js/flickity.pkgd.min.js"></script>
    <script type="text/javascript" src="/assets/js/scrollMonitor.js"></script>
    <script type="text/javascript" src="/assets/js/smooth-scroll.polyfills.js"></script>
    <script type="text/javascript" src="/assets/js/prism.js"></script>
    <script type="text/javascript" src="/assets/js/zoom.min.js"></script>
    <script type="text/javascript" src="/assets/js/bootstrap.js"></script>
    <script type="text/javascript" src="/assets/js/theme.js"></script>
    `;
    $('body').append(scriptsToLoad);
    Session.set('hasLoaded', true);
  }
});
