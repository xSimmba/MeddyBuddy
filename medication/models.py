from django.db import models



class Medication(models.Model):
    """
    Medication model to store information about a user's medication.

    Attributes:
        id (AutoField): Primary key for the medication record.
        user (ForeignKey): Reference to the user who owns the medication.
        name (CharField): Name of the medication.
        dosage (IntegerField): Dosage of the medication.
        instructions (TextField): Instructions for taking the medication.
        created_at (DateTimeField): Timestamp when the medication record was created.
        updated_at (DateTimeField): Timestamp when the medication record was last updated.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dosage = models.IntegerField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
