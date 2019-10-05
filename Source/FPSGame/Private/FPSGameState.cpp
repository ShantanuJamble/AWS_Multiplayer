// Fill out your copyright notice in the Description page of Project Settings.


#include "FPSGameState.h"
#include "FPSPlayerController.h"
#include "Engine/World.h"

void AFPSGameState::MulticastOnMissionComplete_Implementation(APawn* InstigatorPawn, bool IsMissionComplete)
{
	APawn* Pawn = nullptr;

	AFPSPlayerController* Controller = nullptr;
	for (FConstPlayerControllerIterator It = GetWorld()->GetPlayerControllerIterator(); It; ++It)
	{
		Controller = Cast<AFPSPlayerController>(It->Get());

		if (Controller && Controller->IsLocalController())
		{
			Controller->OnMissionComplete(InstigatorPawn, IsMissionComplete);

			Pawn = Controller->GetPawn();

			if (Pawn)
			{
				Pawn->DisableInput(Controller);
			}
		}
	}
}