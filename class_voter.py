class Voters (object):
    
     #initializes voter details
    def _init_ (self, name, age, id_number, account_number):
        self.name = voter_name
        self.age = voter_age
        self.id_number = id_number
        self.__account_number = account_number

    # checks for possible multiple registeration of a voter
    def multiple_registeration(self, id_number):
        self.id_number = []
        if self.id_number.count() > :
            return 'multiple_registeration'
    
    #checks for the age of a voter
    def age_of_voter(self,voter_age):
        if self.age_of_voter < 18:
            return 'invalid registeration'
        else:
            return 'valid registeration'

    #confirms the citizenship of a voter
    def citizenship (self, id_number):
        if id_number == Kenyan:
            return 'valid registeration'
        elif id_number = None:
            return 'invalid registeration'

    #presidential candidate must be a registered voter, therefore inherits from class voter
    class presidential_candidate(voters):

        #checks for academic_qualification of presidential_candidate
        def academic_validity (self, academic_qualification):
            self.academic_qualification = academic_qualification
            if academic_qualification == 'degree'
                return 'valid_candidature'
            else:
               return 'denied'

        #confirms age of presidential candidate    
        def age_requirement (self,age):
            if age => 35
                return 'valid_candidature'
            else:
                return 'denied'

            #confirms that both qualifications for presidential candidate are met
            if academic_qualification != 'degree' and age < 35:
                print ('denied')
            if academic_qualification != 'degree' and age => 35:
                print ('denied')
            if academic_qualification == 'degree' and age < 35:
                print ('denied')
            if academic_qualification == 'degree' and age => 35:
                print ('qualified')
            
           
