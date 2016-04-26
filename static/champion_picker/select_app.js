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

  $scope.team1 = ['', '', '', '', ''];
  $scope.team2 = ['', '', '', '', ''];
  $scope.team1_roles = ['', '', '', '', ''];
  $scope.team2_roles = ['', '', '', '', ''];
  $scope.team1_bans = ['', '', ''];
  $scope.team2_bans = ['', '', ''];

  // hide all roles by default
  $scope.showAll = false;

  $scope.pickChampion = function(team, index) {
    // get best options, show that modal
    $scope.team = team;
    $scope.selected_index = index;
    
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
      console.log($scope.team);
      if (($scope.team === 1 && team2_names.length === 0) || ($scope.team === 2 && team1_names.length === 0)) {
        $('#firstOptionPicker').modal('show');
      } else {
        $('#bestOptionPicker').modal('show');
      }
    }, function (err) {
      $scope.status = 'Error loading data: ' + err.message;
    });
  };

  $scope.selectChampion = function(champion, role) {
    console.log(champion);
    console.log(role);
    console.log($scope.selected_index);
    if (typeof(champion.champion) !== 'undefined') {
      champion = champion.champion;
      if ($scope.team === 1) {
        $scope.team1_roles[$scope.selected_index] = role;
        $scope.team1[$scope.selected_index] = champion;
      } else {
        $scope.team2_roles[$scope.selected_index] = role;
        $scope.team2[$scope.selected_index] = champion;
      }
      $('#bestOptionPicker').modal('hide');
      $('#firstOptionPicker').modal('hide');
    } else {
      var championName;
      championName = champion.role1;

      championFactory.getChampion(championName).then(
      function(res) {
        champion = res.data;
        if ($scope.team === 1) {
          $scope.team1_roles[$scope.selected_index] = role;
          $scope.team1[$scope.selected_index] = champion;
        } else {
          $scope.team2_roles[$scope.selected_index] = role;
          $scope.team2[$scope.selected_index] = champion;
        }
        $('#bestOptionPicker').modal('hide');
        $('#firstOptionPicker').modal('hide');
      }, function(err) {
        $scope.status = err.message;
      });
    }

  }

  $scope.pickAnyChampion = function(team, index) {
    $scope.team = team;
    $scope.selected_index = index;
    $('#champPicker').modal('show'); 
  };

  $scope.banChampion = function(champion) {
    if ($scope.team === 1) {
      $scope.team1_bans[$scope.selected_index] = champion;
    } else {
      $scope.team2_bans[$scope.selected_index] = champion;
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
