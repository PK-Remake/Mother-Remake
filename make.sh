#! /bin/bash

coilsnake-cli compile ./coilsnake-project/ Base.smc MotherRemake.smc
coilsnake-cli createpatch "EarthBound (Expanded).smc" MotherRemake.smc ./Patches/MotherRemake.ips
coilsnake-cli createpatch "EarthBound (Expanded).smc" MotherRemake.smc ./Patches/MotherRemake.ebp ShadowOne333 "Beta patch for the Mother Remake project" "Mother Remake"
