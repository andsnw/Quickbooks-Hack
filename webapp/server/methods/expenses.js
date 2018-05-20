Meteor.methods({
  'expenses/create': (data) => {
    data.lastModified = new Date();
    data.createdAt = new Date();
    Expenses.insert(data);
  },

  'expenses/update': (data) => {

  },

  'expenses/delete': (expenseId) => {
    Expenses.remove(expenseId);
  },
})
