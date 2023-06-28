<template>
  <img id="app" src="@/assets/Footer-min.jpeg" class="border"/>
  <v-toolbar dark app color="black" class="hidden-sm-and-down mt-2">
    <img alt="CSF Logo"  src="@/assets/CSF_Logo_WHITE.png" width="125" height="60" />
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn v-for="item in menu" :key="item.title" :to="item.link" flat>{{
        item.title
      }}</v-btn>
    </v-toolbar-items>
  </v-toolbar>
  <v-toolbar dark app color="black" class="hidden-md-and-up mt-2">
    <img alt="CSF Logo"  src="@/assets/CSF_Logo_WHITE.png" width="125" height="60" />
    <v-spacer></v-spacer>
    <v-dialog v-model="dialog" :fullscreen="mobile" transition="dialog-up-transition">
      <template v-slot:activator="{ props }" >
        <v-btn icon v-bind="props" class="hidden-md-and-up">
          <v-icon :icon="menuBarIcon"></v-icon>
        </v-btn>
      </template>
      <v-card class="overall mt-2">
        <v-toolbar dark app color="black" class="mt-2">
          <img alt="CSF Logo"  src="@/assets/CSF_Logo_WHITE.png" width="125" height="60" />
          <v-spacer></v-spacer>
          <v-btn icon @click="dialog = false" class="hidden-md-and-up">
            <v-icon :icon="closeMenuBarIcon"></v-icon>
          </v-btn>
        </v-toolbar>
        <v-list class="listItem"> 
          <v-list-item
            v-for="(item, index) in menu"
            :key="index"
            :value="index"
            :to="item.link"
            @click="dialog = false"
          >
            <template v-slot:prepend>
              <v-icon v-if="item.icon">{{item.icon}}</v-icon>
            </template>
            <v-list-item-title >{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-card>
    </v-dialog>
  </v-toolbar>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useDisplay } from 'vuetify'
import { aliases } from 'vuetify/iconsets/mdi-svg';

const { mobile } = useDisplay()
const dialog = ref(false)
const menu = [
        { icon: "fa fa-address-card", title: "About Us", link: "/" },
        { icon: "fa fa-chart-line", title: "Dashboard", link: "/"  },
        { icon: "fa fa-trophy", title: "Challenges", link: "/"  },
        { icon: "fa fa-users", title: "Team Page", link: "/"  },
        { icon: "fa fa-calendar", title: "Events", link: "/"  },
        { icon: "fa fa-star", title: "Leaderboards", link: "/"  },
        { icon: "fa fa-sign-in-alt", title: "Login", link: "/"  },
        { icon: "fa fa-pen-square", title: "Sign Up", link: "/signup"  },
]
const menuBarIcon = aliases.menu
const closeMenuBarIcon = aliases.close
</script>
<style>
@import url('https://use.fontawesome.com/releases/v5.15.4/css/all.css');
.hidden-md-and-up {
  padding-right: 3%;
}
.listItem{
  color: white;
  background-color: black;
}
.overall{
  background-color: black;
}
.border {
  height: 100%;
  width: 100%;
  max-height: 15px;
  max-width: 1280px;
  overflow: hidden;
  position: absolute;
  top: 0;
}
</style>