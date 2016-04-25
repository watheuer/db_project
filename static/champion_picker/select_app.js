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

app.factory('matchupFactory', ['$http', function($http) {
  var urlBase = '/matchup/';
  var factory = {};

  factory.postState = function(team1, team2, bans, turn) {
    return $http.post(urlBase, {
        "team1": team1,
        "team2": team2,
        "bans": bans,
        "turn": turn,
    });
  };

  return factory;
}]);

app.controller('champSelectCtrl', ['$scope', 'championFactory', 'matchupFactory', function($scope, championFactory, matchupFactory) {
  getChampions();

  $scope.team1 = ['', '', '', '', '']
  $scope.team2 = ['', '', '', '', '']
  $scope.team1_bans = ['', '', '']
  $scope.team2_bans = ['', '', '']

  $scope.pickChampion = function(team, index) {
    // get best options, show that modal
    $scope.team = team;
    $scope.index = index;
    
    var team1 = $scope.team1.filter(function(val) { return val !== ''; });
    var team2 = $scope.team2.filter(function(val) { return val !== ''; });
    var team1_bans = $scope.team1_bans.filter(function(val) { return val !== ''; });
    var team2_bans = $scope.team2_bans.filter(function(val) { return val !== ''; });
    var bans = team1_bans.concat(team2_bans);
    
    var team1_names = [];
    var team2_names = [];
    var ban_names = [];
    
    for (var i = 0; i < team1.length; i++) {
      team1_names.push(team1[i].name);
    }
    for (var i = 0; i < team2.length; i++) {
      team2_names.push(team2[i].name);
    }
    for (var i = 0; i < bans.length; i++) {
      ban_names.push(bans[i].name);
    }

    matchupFactory.postState(team1_names, team2_names, ban_names, team).then(function (res) {
      $scope.bestPicks = res.data;
    }, function (err) {
      $scope.status = 'Error loading data: ' + err.message;
    });

    $('#bestOptionPicker').modal('show');
  };

  $scope.selectChampion = function(champion) {
    if ($scope.team === 1) {
      $scope.team1[$scope.index] = champion;
    } else {
      $scope.team2[$scope.index] = champion;
    }
    $('#bestOptionPicker').modal('hide');
  }

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
