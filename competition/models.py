from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError


GAME_TYPES = (
	
	('FS', 'foosball'),
)

LOCATION_CHOICES = (
	('H', 'Hostle'),
	('O', 'Office'),
)


class Player(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Competition(models.Model):
	title = models.CharField(max_length=50,null=True,blank=True)
	type = models.CharField(max_length=10, choices=GAME_TYPES)
	place = models.CharField(max_length=10,choices=LOCATION_CHOICES)


class Team(models.Model):
	player1 = models.ForeignKey(Player,on_delete=models.CASCADE, related_name="first")
	player2 = models.ForeignKey(Player,on_delete=models.CASCADE, related_name="second")
	tt_points = models.IntegerField(default=0,blank=True,null=True)
	foosball_points = models.IntegerField(default=0,blank=True,null=True)

	class Meta:
		unique_together = ['player1','player2']

	def validate_unique(self,exclude=None):
		if self.player1==self.player2:
			raise ValidationError('Must have unique players')

		team = Team.objects.filter(player1=self.player2)
		if team.filter(player2=self.player1).exists():
			raise ValidationError('Team already exists')

		models.Model.validate_unique(self,exclude=exclude)


	def save(self, *args, **kwargs):
		self.validate_unique()
		super(Team,self).save(*args, **kwargs)

	def __str__(self):
		return self.player1.__str__() + ',' + self.player2.__str__()


class Match(models.Model):
	team1 = models.ForeignKey(Team,on_delete=models.CASCADE, related_name="team1")
	team2 = models.ForeignKey(Team,on_delete=models.CASCADE, related_name="team2")
	team1_score = models.IntegerField(default=0)
	team2_score = models.IntegerField(default=0)

	game = models.CharField(max_length=10,choices=GAME_TYPES)
	comptn = models.ForeignKey(Competition,on_delete=models.CASCADE,blank=True,null=True,default=None)


	def validate_unique(self,exclude=None):
		p1 = self.team1.player1
		p2 = self.team1.player2
		p3 = self.team2.player1
		p4 = self.team2.player2

		if p3==p1 or p4==p1:
			raise ValidationError('Player cannot exists on both teams')

		if p3==p2 or p4==p2:
			raise ValidationError('Player cannot exists on both teams')

		#match = Match.objects.filter(team2__player=p2)

		models.Model.validate_unique(self,exclude=exclude)


	def save(self, *args, **kwargs):
		self.validate_unique()
		super(Match, self).save(*args, **kwargs)





