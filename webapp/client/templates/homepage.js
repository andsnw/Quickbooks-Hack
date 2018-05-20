Template.homepage.helpers({
  hasData: (collection) => {
    if(collection.count() > 0) {
      return true;
    } else {
      return false;
    }
  },
});
