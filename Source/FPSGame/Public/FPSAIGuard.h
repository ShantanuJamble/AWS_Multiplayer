// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "FPSAIGuard.generated.h"

class UPawnSensingComponent;


UENUM(BlueprintType)
enum class EnemyStates : uint8
{
	Idle,
	Suspicious,
	Alert
};

UCLASS()
class FPSGAME_API AFPSAIGuard : public ACharacter
{
	GENERATED_BODY()

public:
	// Sets default values for this character's properties
	AFPSAIGuard();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	virtual void PostInitializeComponents() override;

	UPROPERTY(VisibleAnywhere, Category = "Component")
	UPawnSensingComponent* PawnSensingComponent;

	UFUNCTION()
	void OnPawnSeen(APawn* Pawn);

	UFUNCTION()
	void OnPawnHeard(APawn* Pawn, const FVector& Location, float volume);

	FRotator OriginalRotation;
	FTimerHandle Timerhandle_ResetRotation;
	UFUNCTION()
	void ResetOrientation();

	UPROPERTY(ReplicatedUsing=OnRep_GuardState)
	EnemyStates guardState;

	UFUNCTION()
	void SetGuardState(EnemyStates state);

	UFUNCTION()
	void OnRep_GuardState();


	UFUNCTION(BlueprintImplementableEvent, Category = "AI")
	void OnStateChanged(EnemyStates state);

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;


};
