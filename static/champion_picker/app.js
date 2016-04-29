var app = angular.module('app', []);

app.factory('championFactory', ['$http', function($http) {
  var urlBase = '/api/champions/';
  var factory = {};

  factory.getChampions = function() {
    return $http.get(urlBase);
  };

  factory.getChampion = function(id) {
    return $http.get(urlBase + id + '/');
  };

  factory.getRoles = function(id) {
    return $http.get(urlBase + id + '/roles/');
  };

  return factory;
}]);

app.factory('roleFactory', ['$http', function($http) {
  var urlBase = '/api/roles/';
  var factory = {};

  factory.getRoles = function() {
    return $http.get(urlBase);
  };

  factory.getRole = function(id) {
    return $http.get(urlBase + id + '/');
  };

  return factory;
}]);

app.factory('buildFactory', ['$http', function($http) {
  var urlBase = '/api/builds/';
  var factory = {};

  factory.getBuilds = function(id) {
    return $http.get(urlBase + id + '/');
  };

  return factory;
}]);

app.controller('champInfoCtrl', ['$scope', 'championFactory', 'buildFactory', function($scope, championFactory, buildFactory) {
  getChampions();
  $scope.selected = '';

  $scope.selectChampion = function(champion) {
    $scope.selected = champion;
    if ($scope.selected !== '') {
      getRoles($scope.selected.name);
    }
  };

  $scope.getBuilds = function(role) {
    $scope.selected_role = role;
    buildFactory.getBuilds(role.id)
      .then(function(res) {
        $scope.builds = res.data;
        $('#builds').modal('show');
        console.log($scope.build);
      }, function(err) {
        $scope.status = 'Error loading data.';
      })
  }

  function getChampions() {
    championFactory.getChampions()
      .then(function(res) {
        $scope.champions = res.data;
        console.log($scope.champions);
      }, function(err) {
        $scope.status = 'Error loading data: ' + err.message;
      });
  }

  function getRoles(name) {
    championFactory.getRoles(name)
      .then(function(res) {
        $scope.roles = res.data;
        console.log($scope.roles);
      }, function(err) {
        $scope.status = 'Error loading data: ' + err.message;
      });
  }
}]);
