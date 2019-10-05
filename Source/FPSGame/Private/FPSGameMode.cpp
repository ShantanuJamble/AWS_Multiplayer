	// Copyright 1998-2017 Epic Games, Inc. All Rights Reserved.

#include "FPSGameMode.h"
#include "FPSHUD.h"
#include "FPSCharacter.h"
#include "FPSGameState.h"
#include "UObject/ConstructorHelpers.h"
#include "Engine/World.h"
#include "Kismet/GameplayStatics.h"

AFPSGameMode::AFPSGameMode()
{
	// set default pawn class to our Blueprinted character
	static ConstructorHelpers::FClassFinder<APawn> PlayerPawnClassFinder(TEXT("/Game/Blueprints/BP_Player"));
	DefaultPawnClass = PlayerPawnClassFinder.Class;

	// use our custom HUD class
	HUDClass = AFPSHUD::StaticClass();
	GameStateClass = AFPSGameState::StaticClass();
}


void AFPSGameMode::CompleteMission(APawn* Pawn, bool MissionSuccess)
{

	if (SpectatingActorClasses &&  Pawn)
	{
		Pawn->DisableInput(nullptr);

		TArray<AActor*> SpectatorList;
		UGameplayStatics::GetAllActorsOfClass(this, SpectatingActorClasses, SpectatorList);

		AActor* NewViewTarget = (SpectatorList.Num() > 0) ? SpectatorList[0] : nullptr;
		if (NewViewTarget)
		{

			for (FConstPlayerControllerIterator It = GetWorld()->GetPlayerControllerIterator(); It; ++It)
			{

				APlayerController* PC = It->Get();
				if (PC)
				{
					PC->SetViewTargetWithBlend(NewViewTarget, 1.0f, EViewTargetBlendFunction::VTBlend_Cubic);
				}
			}
		}

	}

	else
	{
		UE_LOG(LogTemp, Warning, TEXT("SpectatingActorClasses or pawn is null"));
	}



	AFPSGameState* GS = GetGameState<AFPSGameState>();
	if (GS)
	{
		GS->MulticastOnMissionComplete(Pawn, MissionSuccess);
	}
	OnMissionComplete(Pawn, MissionSuccess);
}
