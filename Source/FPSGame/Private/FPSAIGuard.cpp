// Fill out your copyright notice in the Description page of Project Settings.


#include "FPSAIGuard.h"
#include "FPSGameMode.h"
#include "Perception/PawnSensingComponent.h"
#include "DrawDebugHelpers.h"
#include "TimerManager.h"
#include "GameFramework/Actor.h"
// Sets default values
AFPSAIGuard::AFPSAIGuard()
{
 	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	
	PawnSensingComponent = CreateDefaultSubobject<UPawnSensingComponent>(TEXT("PawnSensingCompoenent"));

}

void AFPSAIGuard::PostInitializeComponents()
{
	Super::PostInitializeComponents();
	PawnSensingComponent->OnSeePawn.AddDynamic(this, &AFPSAIGuard::OnPawnSeen);
	PawnSensingComponent->OnHearNoise.AddDynamic(this, &AFPSAIGuard::OnPawnHeard);
}

// Called when the game starts or when spawned
void AFPSAIGuard::BeginPlay()
{
	Super::BeginPlay();
	OriginalRotation = GetActorRotation();
}

void AFPSAIGuard::OnPawnHeard(APawn* Pawn, const FVector& Location, float volume)
{
	if (Pawn == nullptr)
	{
		return;
	}

	DrawDebugSphere(GetWorld(), Pawn->GetTargetLocation(), 32.0f, 12, FColor::Green, false, 10);

	FVector Direction = Location - GetActorLocation();
	Direction.Normalize();

	FRotator lookat = FRotationMatrix::MakeFromX(Direction).Rotator();
	lookat.Pitch = 0.0f;
	lookat.Roll = 0.0f;
	SetActorRotation(lookat);


	GetWorldTimerManager().ClearTimer(Timerhandle_ResetRotation);
	GetWorldTimerManager().SetTimer(Timerhandle_ResetRotation, this, &AFPSAIGuard::ResetOrientation, 3.0f);
}

void AFPSAIGuard::OnPawnSeen(APawn* Pawn)
{

	if (Pawn == nullptr)
	{
		return;
	}
	
	DrawDebugSphere(GetWorld(), Pawn->GetTargetLocation(), 32.0f, 12, FColor::Red, false, 10);
	AFPSGameMode* GameMode = Cast<AFPSGameMode>(GetWorld()->GetAuthGameMode());
	if (GameMode)
		GameMode->CompleteMission(Pawn, false);
}

void AFPSAIGuard::ResetOrientation()
{
	SetActorRotation(OriginalRotation);
}

// Called every frame
void AFPSAIGuard::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}



