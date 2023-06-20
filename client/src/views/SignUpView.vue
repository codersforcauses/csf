<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center" align-content="center">
      <v-col cols="6">
        <v-card>
          <v-card-text>
            <v-form ref="form"> 
              <v-text-field 
                v-model="username" 
                :rules="nameRules" 
                :counter="10" 
                label="Username"
                required
              ></v-text-field>
              <v-text-field 
                v-model="firstname" 
                :rules="nameRules" 
                :counter="10" 
                label="First name"
                required
              ></v-text-field>
              <v-text-field 
                v-model="lastname" 
                :rules="nameRules" 
                :counter="10" 
                label="Last name" 
                required
              ></v-text-field>
              <v-text-field 
                v-model="email" 
                :rules="emailRules" 
                label="E-mail" 
                required
              ></v-text-field>
              <v-text-field 
                v-model="password" 
                :rules="emailRules" 
                label="Password" 
                required
              ></v-text-field>
              <v-row justify="end">
                <v-checkbox-btn
                v-model="teamSignUp"
                :rules="emailRules"
                label="Team Sign Up"
                required
              ></v-checkbox-btn>
                <v-checkbox-btn
                v-model="hasConsent"
                :rules="emailRules"
                label="Has Consent"
                required
              ></v-checkbox-btn>
              </v-row>
            </v-form>
          </v-card-text>
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
    }
  }
}
</script>