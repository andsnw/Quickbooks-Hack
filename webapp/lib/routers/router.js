
Router.route('/', {
  name: 'homepage',
  layoutTemplate: 'mainLayout',
  data: () => {
    return {
      entries: Expenses.find({}),
    };
  },
});


Router.route( "/create", function() {

  this.response.setHeader( 'Access-Control-Allow-Origin', '*' );
  API.handleRequest( this, 'create', this.request.method );
}, { where: 'server' });
