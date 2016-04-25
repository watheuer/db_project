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

app.controller('champSelectCtrl', ['$scope', 'championFactory', function($scope, championFactory) {
  getChampions();

  $scope.team1 = ['', '', '', '', '']
  $scope.team2 = ['', '', '', '', '']
  $scope.team1_bans = ['', '', '']
  $scope.team2_bans = ['', '', '']

  $scope.pickChampion = function(team, index) {
    // get best options, show that modal
    $('#bestOptionPicker').modal('show');
  };

  $scope.pickAnyChampion = function(team, index) {
    $scope.team = team;
    $scope.index = index;
    $('#champPicker').modal('show'); 
  };

  $scope.banChampion = function(champion) {
    if ($scope.team === 1) {
      $scope.team1_bans[$scope.index] = champion;
    } else {
      $scope.team2_bans[$scope.index] = champion;
    }
    $('#champPicker').modal('hide'); 
  };

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
