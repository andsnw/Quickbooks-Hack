API = {
  connection: function( request ) {
   var getRequestContents = API.utility.getRequestContents( request );

   return { data: getRequestContents };
 },
  handleRequest: function( context, resource, method ) {
    var connection = API.connection( context.request );
    if ( !connection.error ) {
      API.methods[ resource ][ method ]( context, connection );
    } else {
      API.utility.response( context, 401, connection );
    }
  },
  methods: {
    create: {
      GET: function( context, connection ) {},
      POST: function( context, connection ) {
        // var hasData   = API.utility.hasData( connection.data ),
            // validData = API.utility.validate( connection.data, { "name": String, "crust": String, "toppings": [ String ] });
        var currentData = connection.data;

        currentData.createdAt = new Date();
        currentData.lastModifier = new Date();


        console.log(currentData);
        if (!currentData.params.hasOwnProperty('spent-detail')) {
          API.utility.response( context, 500, { "message": "Error!" } );
          return false;
        }
        Expenses.insert(currentData);
        API.utility.response( context, 200, { "message": "Successfully created expense!" } );
        // if ( hasData && validData ) {
        //   connection.data.owner = connection.owner;
        //   var pizza = Pizza.insert( connection.data );
        //   API.utility.response( context, 200, { "_id": pizza, "message": "Pizza successfully created!" } );
        // } else {
        //   API.utility.response( context, 403, { error: 403, message: "POST calls must have a name, crust, and toppings passed in the request body in the correct formats." } );
        // }
      },

      PUT: function( context, connection ) {},
      DELETE: function( context, connection ) {}
    }
  },

  utility: {
    getRequestContents: function( request ) {
      switch( request.method ) {
        case "GET":
          return request.query;
        case "POST":
        case "PUT":
        case "DELETE":
          return request.body;
      }
    },
    hasData: function( data ) {},
    response: function( context, statusCode, data ) {
      context.response.setHeader( 'Content-Type', 'application/json' );
      context.response.statusCode = statusCode;
      context.response.end( JSON.stringify( data ) );

    },
    validate: function( data, pattern ) {}
  }
};
