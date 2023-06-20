<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center" align-content="center">
      <v-col xs="12" md="6">
        <v-card class="pa-10">
            <v-form ref="form" @submit.prevent> 
              <v-text-field 
                v-model="username" 
                :counter="25" 
                label="Username"
                required
              ></v-text-field>
              <v-text-field 
                v-model="firstname" 
                :counter="25" 
                label="First name"
                required
              ></v-text-field>
              <v-text-field 
                v-model="lastname" 
                :counter="25" 
                label="Last name" 
                required
              ></v-text-field>
              <v-text-field 
                v-model="email"  
                :counter="25" 
                label="E-mail" 
                required
              ></v-text-field>
              <v-text-field 
                v-model="password" 
                label="Password" 
                required
              ></v-text-field>
              <v-row justify="center">
                <v-checkbox
                v-model="teamSignUp"
                label="Team Sign Up"
                
                required
              ></v-checkbox>
                <v-checkbox
                v-model="hasConsent"
                label="Has Consent"
                hint="Does CSF have permission to use their data?"
                :persistent-hint="true"
                required
              ></v-checkbox>
              </v-row>
              <v-row>
                <v-btn type="submit" block class="mt-2">Submit</v-btn>
              </v-row>
            </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">

export default {
  name: "SignUpView",
  setup() {
    return {

    }
  },
  data() {
    return {
      username: '',
      firstname: '',
      lastname: '',
      email: '',
      password: '',
      teamSignUp: false,
      hasConsent: false
      // validation rules - might want to use a specialized component
      // like Vee-validate or vuelidate

    }
  }
}
</script>